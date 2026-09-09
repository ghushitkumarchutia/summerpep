import { chatService } from "../../services/chat.service.js";
import { EVENTS } from "../../config/constants.js";
import { env } from "../../config/environment.js";
import { sanitizeText } from "../../utils/sanitizer.js";
import { validateMessage, isPlainObject } from "../../utils/validator.js";
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
  );

  io.to(user.room).emit(EVENTS.RECEIVE_MESSAGE, message);
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
