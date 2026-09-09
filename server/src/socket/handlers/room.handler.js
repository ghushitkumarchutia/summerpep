import { chatService } from "../../services/chat.service.js";
import { EVENTS, LIMITS, SYSTEM_USER } from "../../config/constants.js";
import { sanitizeUsername, sanitizeRoomName } from "../../utils/sanitizer.js";
import {
  validateUsername,
  validateRoomName,
  isPlainObject,
} from "../../utils/validator.js";

export const handleJoinRoom = (io, socket, payload) => {
  if (!isPlainObject(payload)) {
    socket.emit(EVENTS.ERROR, { message: "Invalid payload format" });
    return;
  }

  const rawUsername = payload.username;
  const rawRoom = payload.room || LIMITS.DEFAULT_ROOM;

  const username = sanitizeUsername(rawUsername);
  const room = sanitizeRoomName(rawRoom) || LIMITS.DEFAULT_ROOM;

  const usernameValidation = validateUsername(username);
  if (!usernameValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: usernameValidation.error });
    return;
  }

  const roomValidation = validateRoomName(room);
  if (!roomValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: roomValidation.error });
    return;
  }

  const currentUser = chatService.getUser(socket.id);
  if (currentUser) {
    socket.leave(currentUser.room);
    const leaveResult = chatService.leaveRoom(socket.id);
    if (leaveResult && leaveResult.remainingUsers.length > 0) {
      socket.to(leaveResult.roomName).emit(EVENTS.USER_LEFT, {
        user: leaveResult.user,
        users: leaveResult.remainingUsers,
      });
      const leaveMessage = chatService.addMessage(
        leaveResult.roomName,
        SYSTEM_USER,
        `${leaveResult.user.username} left the room`,
        "system",
      );
      io.to(leaveResult.roomName).emit(EVENTS.RECEIVE_MESSAGE, leaveMessage);
    }
  }

  const joinResult = chatService.joinRoom(socket.id, username, room);
  socket.join(room);

  socket.emit(EVENTS.ROOM_DATA, {
    room: joinResult.roomName,
    users: joinResult.users,
    history: joinResult.history,
  });

  socket.to(room).emit(EVENTS.USER_JOINED, {
    user: joinResult.user,
    users: joinResult.users,
  });

  const systemMessage = chatService.addMessage(
    room,
    SYSTEM_USER,
    `${username} joined the room`,
    "system",
  );
  io.to(room).emit(EVENTS.RECEIVE_MESSAGE, systemMessage);
};

export const handleLeaveRoom = (io, socket) => {
  const leaveResult = chatService.leaveRoom(socket.id);
  if (!leaveResult) return;

  socket.leave(leaveResult.roomName);

  if (leaveResult.remainingUsers.length > 0) {
    socket.to(leaveResult.roomName).emit(EVENTS.USER_LEFT, {
      user: leaveResult.user,
      users: leaveResult.remainingUsers,
    });

    const systemMessage = chatService.addMessage(
      leaveResult.roomName,
      SYSTEM_USER,
      `${leaveResult.user.username} left the room`,
      "system",
    );
    io.to(leaveResult.roomName).emit(EVENTS.RECEIVE_MESSAGE, systemMessage);
  }
};
