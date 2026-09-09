const HTML_ESCAPE_MAP = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#x27;",
  "/": "&#x2F;",
};

const HTML_REGEX = /[&<>"'/]/g;
const CONTROL_CHARS_REGEX = /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g;
const MULTIPLE_SPACES_REGEX = /\s+/g;
const ROOM_INVALID_CHARS_REGEX = /[^a-zA-Z0-9_-]/g;

export const escapeHtml = (text) => {
  if (typeof text !== "string") return "";
  return text.replace(HTML_REGEX, (match) => HTML_ESCAPE_MAP[match]);
};

export const sanitizeText = (text) => {
  if (typeof text !== "string") return "";
  const cleaned = text.replace(CONTROL_CHARS_REGEX, "").trim();
  return escapeHtml(cleaned);
};

export const sanitizeUsername = (username) => {
  if (typeof username !== "string") return "";
  const cleaned = username
    .replace(CONTROL_CHARS_REGEX, "")
    .replace(MULTIPLE_SPACES_REGEX, " ")
    .trim();
  return escapeHtml(cleaned);
};

export const sanitizeRoomName = (room) => {
  if (typeof room !== "string") return "";
  return room
    .replace(CONTROL_CHARS_REGEX, "")
    .trim()
    .toLowerCase()
    .replace(ROOM_INVALID_CHARS_REGEX, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
};
