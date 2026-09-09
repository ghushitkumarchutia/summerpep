import { chatService } from "../../services/chat.service.js";
import { EVENTS } from "../../config/constants.js";
import { env } from "../../config/environment.js";
import { sanitizeText } from "../../utils/sanitizer.js";
import {
  validateMessage,
  validateMessageId,
  isPlainObject,
} from "../../utils/validator.js";
import { checkSocketRateLimit } from "../middlewares/socket-ratelimit.middleware.js";

export const handleSendMessage = (io, socket, payload) => {
  if (!checkSocketRateLimit(socket)) return;

  const user = chatService.getUser(socket.id);
  if (!user) {
    socket.emit(EVENTS.ERROR, { message: "You must join a room first" });
    return;
  }

  if (!isPlainObject(payload)) {
    socket.emit(EVENTS.ERROR, { message: "Invalid message payload format" });
    return;
  }

  const rawContent = payload.content;
  const validation = validateMessage(rawContent, env.MAX_MESSAGE_LENGTH);
  if (!validation.valid) {
    socket.emit(EVENTS.ERROR, { message: validation.error });
    return;
  }

  let replyToId = null;
  if (payload.replyToId) {
    const replyValidation = validateMessageId(payload.replyToId);
    if (!replyValidation.valid) {
      socket.emit(EVENTS.ERROR, { message: replyValidation.error });
      return;
    }
    replyToId = payload.replyToId;
  }

  const content = sanitizeText(rawContent);
  if (!content) {
    socket.emit(EVENTS.ERROR, { message: "Message content cannot be empty" });
    return;
  }

  const message = chatService.addMessage(
    user.room,
    { socketId: socket.id, username: user.username },
    content,
    "user",
    replyToId,
  );

  io.to(user.room).emit(EVENTS.RECEIVE_MESSAGE, message);
};

export const handleEditMessage = (io, socket, payload) => {
  if (!checkSocketRateLimit(socket)) return;

  const user = chatService.getUser(socket.id);
  if (!user) {
    socket.emit(EVENTS.ERROR, { message: "You must join a room first" });
    return;
  }

  if (!isPlainObject(payload)) {
    socket.emit(EVENTS.ERROR, { message: "Invalid payload format" });
    return;
  }

  const messageIdValidation = validateMessageId(payload.messageId);
  if (!messageIdValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: messageIdValidation.error });
    return;
  }

  const contentValidation = validateMessage(
    payload.content,
    env.MAX_MESSAGE_LENGTH,
  );
  if (!contentValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: contentValidation.error });
    return;
  }

  const sanitizedContent = sanitizeText(payload.content);
  if (!sanitizedContent) {
    socket.emit(EVENTS.ERROR, { message: "Message content cannot be empty" });
    return;
  }

  const result = chatService.editMessage(
    user.room,
    payload.messageId,
    socket.id,
    sanitizedContent,
  );
  if (!result.success) {
    socket.emit(EVENTS.ERROR, { message: result.error });
    return;
  }

  io.to(user.room).emit(EVENTS.MESSAGE_EDITED, result.message);
};

export const handleDeleteMessage = (io, socket, payload) => {
  if (!checkSocketRateLimit(socket)) return;

  const user = chatService.getUser(socket.id);
  if (!user) {
    socket.emit(EVENTS.ERROR, { message: "You must join a room first" });
    return;
  }

  if (!isPlainObject(payload)) {
    socket.emit(EVENTS.ERROR, { message: "Invalid payload format" });
    return;
  }

  const messageIdValidation = validateMessageId(payload.messageId);
  if (!messageIdValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: messageIdValidation.error });
    return;
  }

  const result = chatService.deleteMessage(
    user.room,
    payload.messageId,
    socket.id,
  );
  if (!result.success) {
    socket.emit(EVENTS.ERROR, { message: result.error });
    return;
  }

  io.to(user.room).emit(EVENTS.MESSAGE_DELETED, {
    messageId: result.messageId,
    deletedAt: result.deletedAt,
  });
};

export const handleTypingStart = (io, socket) => {
  const user = chatService.getUser(socket.id);
  if (!user) return;

  socket.to(user.room).emit(EVENTS.USER_TYPING, {
    username: user.username,
    isTyping: true,
  });
};

export const handleTypingStop = (io, socket) => {
  const user = chatService.getUser(socket.id);
  if (!user) return;

  socket.to(user.room).emit(EVENTS.USER_TYPING, {
    username: user.username,
    isTyping: false,
  });
};
