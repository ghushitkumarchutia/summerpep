import { chatService } from "../services/chat.service.js";

export const getHealth = (req, res) => {
  const stats = chatService.getStats();

  res.status(200).json({
    status: "ok",
    uptime: Math.floor(process.uptime()),
    timestamp: new Date().toISOString(),
    stats,
  });
};
