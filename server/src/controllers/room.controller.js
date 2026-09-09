import { chatService } from "../services/chat.service.js";
import { sanitizeRoomName } from "../utils/sanitizer.js";
import { validateRoomName, validateMessageId } from "../utils/validator.js";

export const getActiveRooms = (req, res) => {
  const rooms = chatService.getActiveRooms();

  res.status(200).json({
    success: true,
    count: rooms.length,
    rooms,
  });
};

export const getRoomInfo = (req, res) => {
  const sanitized = sanitizeRoomName(req.params.room);
  const validation = validateRoomName(sanitized);

  if (!validation.valid) {
    res.status(400).json({
      success: false,
      error: validation.error,
    });
    return;
  }

  const users = chatService.getRoomUsers(sanitized);
  const messages = chatService.getRoomMessages(sanitized);

  res.status(200).json({
    success: true,
    room: sanitized,
    userCount: users.length,
    users,
    messageCount: messages.length,
  });
};

export const getMessageDetails = (req, res) => {
  const sanitizedRoom = sanitizeRoomName(req.params.room);
  const roomValidation = validateRoomName(sanitizedRoom);

  if (!roomValidation.valid) {
    res.status(400).json({
      success: false,
      error: roomValidation.error,
    });
    return;
  }

  const idValidation = validateMessageId(req.params.messageId);
  if (!idValidation.valid) {
    res.status(400).json({
      success: false,
      error: idValidation.error,
    });
    return;
  }

  const message = chatService.getMessageById(
    sanitizedRoom,
    req.params.messageId,
  );
  if (!message) {
    res.status(404).json({
      success: false,
      error: "Message not found",
    });
    return;
  }

  res.status(200).json({
    success: true,
    message: {
      ...message,
      reactions: chatService.formatReactions(message.reactions),
    },
  });
};

export const getThreadMessages = (req, res) => {
  const sanitizedRoom = sanitizeRoomName(req.params.room);
  const roomValidation = validateRoomName(sanitizedRoom);

  if (!roomValidation.valid) {
    res.status(400).json({
      success: false,
      error: roomValidation.error,
    });
    return;
  }

  const idValidation = validateMessageId(req.params.messageId);
  if (!idValidation.valid) {
    res.status(400).json({
      success: false,
      error: idValidation.error,
    });
    return;
  }

  const thread = chatService.getMessageThread(
    sanitizedRoom,
    req.params.messageId,
  );
  if (!thread) {
    res.status(404).json({
      success: false,
      error: "Parent message not found",
    });
    return;
  }

  res.status(200).json({
    success: true,
    parent: {
      ...thread.parent,
      reactions: chatService.formatReactions(thread.parent.reactions),
    },
    replyCount: thread.replies.length,
    replies: thread.replies,
  });
};
