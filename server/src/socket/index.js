import { Server } from "socket.io";
import { env } from "../config/environment.js";
import { EVENTS } from "../config/constants.js";
import { handleJoinRoom, handleLeaveRoom } from "./handlers/room.handler.js";
import {
  handleSendMessage,
  handleEditMessage,
  handleDeleteMessage,
  handleTypingStart,
  handleTypingStop,
} from "./handlers/message.handler.js";
import {
  handleAddReaction,
  handleRemoveReaction,
} from "./handlers/reaction.handler.js";
import { handleDisconnect } from "./handlers/disconnect.handler.js";

export const initializeSocket = (httpServer) => {
  const io = new Server(httpServer, {
    cors: {
      origin:
        env.CORS_ORIGIN === "*"
          ? "*"
          : env.CORS_ORIGIN.split(",").map((o) => o.trim()),
      methods: ["GET", "POST"],
    },
    maxHttpBufferSize: 64 * 1024,
    pingTimeout: 20000,
    pingInterval: 25000,
  });

  io.on(EVENTS.CONNECTION, (socket) => {
    socket.on(EVENTS.JOIN_ROOM, (payload) => {
      handleJoinRoom(io, socket, payload);
    });

    socket.on(EVENTS.LEAVE_ROOM, () => {
      handleLeaveRoom(io, socket);
    });

    socket.on(EVENTS.SEND_MESSAGE, (payload) => {
      handleSendMessage(io, socket, payload);
    });

    socket.on(EVENTS.EDIT_MESSAGE, (payload) => {
      handleEditMessage(io, socket, payload);
    });

    socket.on(EVENTS.DELETE_MESSAGE, (payload) => {
      handleDeleteMessage(io, socket, payload);
    });

    socket.on(EVENTS.ADD_REACTION, (payload) => {
      handleAddReaction(io, socket, payload);
    });

    socket.on(EVENTS.REMOVE_REACTION, (payload) => {
      handleRemoveReaction(io, socket, payload);
    });

    socket.on(EVENTS.TYPING_START, () => {
      handleTypingStart(io, socket);
    });

    socket.on(EVENTS.TYPING_STOP, () => {
      handleTypingStop(io, socket);
    });

    socket.on(EVENTS.DISCONNECT, () => {
      handleDisconnect(io, socket);
    });

    socket.on("error", () => {
      socket.emit(EVENTS.ERROR, { message: "Internal socket error occurred" });
    });
  });

  return io;
};
