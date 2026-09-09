import { chatService } from "../../services/chat.service.js";
import { EVENTS, SYSTEM_USER } from "../../config/constants.js";
import { socketRateLimiter } from "../middlewares/socket-ratelimit.middleware.js";

export const handleDisconnect = (io, socket) => {
  socketRateLimiter.remove(socket.id);

  const leaveResult = chatService.leaveRoom(socket.id);
  if (!leaveResult) return;

  if (leaveResult.remainingUsers.length > 0) {
    socket.to(leaveResult.roomName).emit(EVENTS.USER_LEFT, {
      user: leaveResult.user,
      users: leaveResult.remainingUsers
    });

    const systemMessage = chatService.addMessage(
      leaveResult.roomName,
      SYSTEM_USER,
      `${leaveResult.user.username} disconnected`,
      "system"
    );

    io.to(leaveResult.roomName).emit(EVENTS.RECEIVE_MESSAGE, systemMessage);
  }
};
