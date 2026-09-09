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

  formatReactions(reactionsMap = {}) {
    const formatted = {};
    for (const [emoji, users] of Object.entries(reactionsMap)) {
      formatted[emoji] = {
        count: users.length,
        users: [...users],
      };
    }
    return formatted;
  }

  addMessage(roomName, sender, content, type = "user", replyToId = null) {
    const room = this.getOrCreateRoom(roomName);

    let replyData = null;
    if (replyToId) {
      const parent = room.messages.find((m) => m.id === replyToId);
      if (parent && parent.type !== "system") {
        replyData = {
          id: parent.id,
          sender: parent.sender.username,
          snippet: parent.content.slice(0, 100),
        };
      }
    }

    const message = {
      id: randomUUID(),
      room: roomName,
      sender: {
        id: sender.id || sender.socketId,
        username: sender.username,
      },
      content,
      type,
      replyTo: replyData,
      reactions: {},
      isEdited: false,
      editedAt: null,
      isDeleted: false,
      deletedAt: null,
      timestamp: new Date().toISOString(),
    };

    room.messages.push(message);

    if (room.messages.length > env.MAX_ROOM_HISTORY) {
      room.messages.splice(0, room.messages.length - env.MAX_ROOM_HISTORY);
    }

    return message;
  }

  getMessageById(roomName, messageId) {
    const room = this.rooms.get(roomName);
    if (!room) return null;
    return room.messages.find((m) => m.id === messageId) || null;
  }

  addReaction(roomName, messageId, emoji, username) {
    const message = this.getMessageById(roomName, messageId);
    if (!message || message.isDeleted) {
      return { success: false, error: "Message not found or deleted" };
    }

    if (!message.reactions) {
      message.reactions = {};
    }

    const reactionKeys = Object.keys(message.reactions);
    if (
      reactionKeys.length >= LIMITS.MAX_REACTIONS_PER_MESSAGE &&
      !message.reactions[emoji]
    ) {
      return {
        success: false,
        error: "Maximum unique reactions reached for this message",
      };
    }

    if (!message.reactions[emoji]) {
      message.reactions[emoji] = [];
    }

    if (message.reactions[emoji].includes(username)) {
      return { success: false, error: "User already reacted with this emoji" };
    }

    message.reactions[emoji].push(username);

    return {
      success: true,
      messageId,
      reactions: this.formatReactions(message.reactions),
    };
  }

  removeReaction(roomName, messageId, emoji, username) {
    const message = this.getMessageById(roomName, messageId);
    if (!message || !message.reactions || !message.reactions[emoji]) {
      return { success: false, error: "Reaction not found" };
    }

    const index = message.reactions[emoji].indexOf(username);
    if (index === -1) {
      return { success: false, error: "User has not reacted with this emoji" };
    }

    message.reactions[emoji].splice(index, 1);
    if (message.reactions[emoji].length === 0) {
      delete message.reactions[emoji];
    }

    return {
      success: true,
      messageId,
      reactions: this.formatReactions(message.reactions),
    };
  }

  editMessage(roomName, messageId, socketId, newContent) {
    const message = this.getMessageById(roomName, messageId);
    if (!message) {
      return { success: false, error: "Message not found" };
    }

    if (message.type === "system" || message.isDeleted) {
      return { success: false, error: "Cannot edit this message" };
    }

    if (message.sender.id !== socketId) {
      return {
        success: false,
        error: "Unauthorized: only message author can edit",
      };
    }

    message.content = newContent;
    message.isEdited = true;
    message.editedAt = new Date().toISOString();

    return {
      success: true,
      message,
    };
  }

  deleteMessage(roomName, messageId, socketId) {
    const message = this.getMessageById(roomName, messageId);
    if (!message) {
      return { success: false, error: "Message not found" };
    }

    if (message.type === "system") {
      return { success: false, error: "Cannot delete system messages" };
    }

    if (message.sender.id !== socketId) {
      return {
        success: false,
        error: "Unauthorized: only message author can delete",
      };
    }

    message.isDeleted = true;
    message.content = "This message was deleted";
    message.deletedAt = new Date().toISOString();
    message.reactions = {};

    return {
      success: true,
      messageId,
      deletedAt: message.deletedAt,
    };
  }

  getMessageThread(roomName, messageId) {
    const room = this.rooms.get(roomName);
    if (!room) return null;

    const parent = room.messages.find((m) => m.id === messageId);
    if (!parent) return null;

    const replies = room.messages.filter(
      (m) => m.replyTo && m.replyTo.id === messageId,
    );

    return {
      parent,
      replies,
    };
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
