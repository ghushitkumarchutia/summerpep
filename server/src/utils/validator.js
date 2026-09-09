import { LIMITS } from "../config/constants.js";
import { env } from "../config/environment.js";

export const isPlainObject = (value) => {
  return typeof value === "object" && value !== null && !Array.isArray(value);
};

export const validateUsername = (username) => {
  if (typeof username !== "string") {
    return { valid: false, error: "Username must be a string" };
  }
  const length = username.length;
  if (
    length < LIMITS.MIN_USERNAME_LENGTH ||
    length > LIMITS.MAX_USERNAME_LENGTH
  ) {
    return {
      valid: false,
      error: `Username must be between ${LIMITS.MIN_USERNAME_LENGTH} and ${LIMITS.MAX_USERNAME_LENGTH} characters`,
    };
  }
  return { valid: true };
};

export const validateRoomName = (room) => {
  if (typeof room !== "string") {
    return { valid: false, error: "Room name must be a string" };
  }
  const length = room.length;
  if (length < LIMITS.MIN_ROOM_LENGTH || length > LIMITS.MAX_ROOM_LENGTH) {
    return {
      valid: false,
      error: `Room name must be between ${LIMITS.MIN_ROOM_LENGTH} and ${LIMITS.MAX_ROOM_LENGTH} characters`,
    };
  }
  return { valid: true };
};

export const validateMessage = (
  content,
  maxLength = env.MAX_MESSAGE_LENGTH,
) => {
  if (typeof content !== "string") {
    return { valid: false, error: "Message content must be a string" };
  }
  const length = content.length;
  if (length === 0) {
    return { valid: false, error: "Message content cannot be empty" };
  }
  if (length > maxLength) {
    return {
      valid: false,
      error: `Message content cannot exceed ${maxLength} characters`,
    };
  }
  return { valid: true };
};
