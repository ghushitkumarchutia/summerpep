import { env } from "../../config/environment.js";
import { EVENTS } from "../../config/constants.js";

class SocketRateLimiter {
  constructor() {
    this.records = new Map();
  }

  isRateLimited(socketId) {
    const now = Date.now();
    const windowStart = now - env.SOCKET_RATE_LIMIT_WINDOW_MS;

    let timestamps = this.records.get(socketId) || [];
    timestamps = timestamps.filter((timestamp) => timestamp > windowStart);

    if (timestamps.length >= env.SOCKET_RATE_LIMIT_MAX) {
      this.records.set(socketId, timestamps);
      return true;
    }

    timestamps.push(now);
    this.records.set(socketId, timestamps);
    return false;
  }

  remove(socketId) {
    this.records.delete(socketId);
  }
}

export const socketRateLimiter = new SocketRateLimiter();

export const checkSocketRateLimit = (socket) => {
  if (socketRateLimiter.isRateLimited(socket.id)) {
    socket.emit(EVENTS.ERROR, {
      message: "Rate limit exceeded. Please slow down.",
    });
    return false;
  }
  return true;
};
