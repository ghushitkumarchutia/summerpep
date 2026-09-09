import { LIMITS } from "../config/constants.js";
import { env } from "../config/environment.js";

const EMOJI_REGEX = /^\p{Extended_Pictographic}+$/u;
const UUID_REGEX =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

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

export const validateEmoji = (emoji) => {
  if (typeof emoji !== "string") {
    return { valid: false, error: "Emoji must be a string" };
  }
  const trimmed = emoji.trim();
  if (trimmed.length === 0 || trimmed.length > LIMITS.MAX_EMOJI_LENGTH) {
    return {
      valid: false,
      error: `Emoji length must be between 1 and ${LIMITS.MAX_EMOJI_LENGTH} characters`,
    };
  }
  if (!EMOJI_REGEX.test(trimmed)) {
    return { valid: false, error: "Invalid emoji character" };
  }
  return { valid: true };
};

export const validateMessageId = (id) => {
  if (typeof id !== "string") {
    return { valid: false, error: "Message ID must be a string" };
  }
  if (!UUID_REGEX.test(id)) {
    return { valid: false, error: "Invalid message ID format" };
  }
  return { valid: true };
};
