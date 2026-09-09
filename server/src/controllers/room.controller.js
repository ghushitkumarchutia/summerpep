import { chatService } from "../services/chat.service.js";
import { sanitizeRoomName } from "../utils/sanitizer.js";
import { validateRoomName } from "../utils/validator.js";

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
