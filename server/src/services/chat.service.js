import { randomUUID } from "node:crypto";
import { env } from "../config/environment.js";
import { LIMITS } from "../config/constants.js";

class ChatService {
  constructor() {
    this.rooms = new Map();
    this.users = new Map();
  }

  getOrCreateRoom(roomName) {
    if (!this.rooms.has(roomName)) {
      this.rooms.set(roomName, {
        name: roomName,
        users: new Map(),
        messages: [],
        createdAt: Date.now(),
      });
    }
    return this.rooms.get(roomName);
  }

  joinRoom(socketId, username, roomName) {
    if (this.users.has(socketId)) {
      this.leaveRoom(socketId);
    }

    const room = this.getOrCreateRoom(roomName);
    const user = {
      socketId,
      username,
      room: roomName,
      joinedAt: new Date().toISOString(),
    };

    room.users.set(socketId, user);
    this.users.set(socketId, user);

    const usersList = Array.from(room.users.values()).map(
      ({ socketId: sid, username: uname, joinedAt }) => ({
        socketId: sid,
        username: uname,
        joinedAt,
      }),
    );

    return {
      user,
      roomName,
      users: usersList,
      history: [...room.messages],
    };
  }

  leaveRoom(socketId) {
    const user = this.users.get(socketId);
    if (!user) return null;

    const roomName = user.room;
    const room = this.rooms.get(roomName);

    this.users.delete(socketId);

    if (room) {
      room.users.delete(socketId);

      if (room.users.size === 0 && roomName !== LIMITS.DEFAULT_ROOM) {
        this.rooms.delete(roomName);
      }
    }

    const remainingUsers = room
      ? Array.from(room.users.values()).map(
          ({ socketId: sid, username: uname, joinedAt }) => ({
            socketId: sid,
            username: uname,
            joinedAt,
          }),
        )
      : [];

    return {
      user,
      roomName,
      remainingUsers,
    };
  }

  addMessage(roomName, sender, content, type = "user") {
    const room = this.getOrCreateRoom(roomName);
    const message = {
      id: randomUUID(),
      room: roomName,
      sender: {
        id: sender.id || sender.socketId,
        username: sender.username,
      },
      content,
      type,
      timestamp: new Date().toISOString(),
    };

    room.messages.push(message);

    if (room.messages.length > env.MAX_ROOM_HISTORY) {
      room.messages.splice(0, room.messages.length - env.MAX_ROOM_HISTORY);
    }

    return message;
  }

  getUser(socketId) {
    return this.users.get(socketId) || null;
  }

  getRoomUsers(roomName) {
    const room = this.rooms.get(roomName);
    if (!room) return [];
    return Array.from(room.users.values()).map(
      ({ socketId, username, joinedAt }) => ({
        socketId,
        username,
        joinedAt,
      }),
    );
  }

  getRoomMessages(roomName) {
    const room = this.rooms.get(roomName);
    return room ? [...room.messages] : [];
  }

  getActiveRooms() {
    const list = [];
    for (const [name, room] of this.rooms.entries()) {
      list.push({
        name,
        userCount: room.users.size,
        messageCount: room.messages.length,
        createdAt: room.createdAt,
      });
    }
    return list;
  }

  getStats() {
    return {
      activeUsers: this.users.size,
      activeRooms: this.rooms.size,
    };
  }
}

export const chatService = new ChatService();
