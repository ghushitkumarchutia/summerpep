import { chatService } from "../../services/chat.service.js";
import { EVENTS } from "../../config/constants.js";
import {
  isPlainObject,
  validateEmoji,
  validateMessageId,
} from "../../utils/validator.js";
import { checkSocketRateLimit } from "../middlewares/socket-ratelimit.middleware.js";

export const handleAddReaction = (io, socket, payload) => {
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

  const emojiValidation = validateEmoji(payload.emoji);
  if (!emojiValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: emojiValidation.error });
    return;
  }

  const result = chatService.addReaction(
    user.room,
    payload.messageId,
    payload.emoji.trim(),
    user.username,
  );

  if (!result.success) {
    socket.emit(EVENTS.ERROR, { message: result.error });
    return;
  }

  io.to(user.room).emit(EVENTS.REACTION_UPDATED, {
    messageId: result.messageId,
    reactions: result.reactions,
  });
};

export const handleRemoveReaction = (io, socket, payload) => {
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

  const emojiValidation = validateEmoji(payload.emoji);
  if (!emojiValidation.valid) {
    socket.emit(EVENTS.ERROR, { message: emojiValidation.error });
    return;
  }

  const result = chatService.removeReaction(
    user.room,
    payload.messageId,
    payload.emoji.trim(),
    user.username,
  );

  if (!result.success) {
    socket.emit(EVENTS.ERROR, { message: result.error });
    return;
  }

  io.to(user.room).emit(EVENTS.REACTION_UPDATED, {
    messageId: result.messageId,
    reactions: result.reactions,
  });
};
