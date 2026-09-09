import "dotenv/config";
import { LIMITS } from "./constants.js";

const parseInteger = (value, fallback) => {
  const parsed = parseInt(value, 10);
  return Number.isInteger(parsed) && parsed > 0 ? parsed : fallback;
};

export const env = Object.freeze({
  PORT: parseInteger(process.env.PORT, 4000),
  NODE_ENV: process.env.NODE_ENV || "development",
  CORS_ORIGIN: process.env.CORS_ORIGIN || "*",
  MAX_ROOM_HISTORY: parseInteger(
    process.env.MAX_ROOM_HISTORY,
    LIMITS.DEFAULT_MAX_ROOM_HISTORY,
  ),
  MAX_MESSAGE_LENGTH: parseInteger(
    process.env.MAX_MESSAGE_LENGTH,
    LIMITS.DEFAULT_MAX_MESSAGE_LENGTH,
  ),
  RATE_LIMIT_WINDOW_MS: parseInteger(process.env.RATE_LIMIT_WINDOW_MS, 60000),
  RATE_LIMIT_MAX: parseInteger(process.env.RATE_LIMIT_MAX, 100),
  SOCKET_RATE_LIMIT_WINDOW_MS: parseInteger(
    process.env.SOCKET_RATE_LIMIT_WINDOW_MS,
    2000,
  ),
  SOCKET_RATE_LIMIT_MAX: parseInteger(process.env.SOCKET_RATE_LIMIT_MAX, 10),
});
