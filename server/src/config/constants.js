export const EVENTS = Object.freeze({
  CONNECTION: "connection",
  DISCONNECT: "disconnect",
  JOIN_ROOM: "join_room",
  LEAVE_ROOM: "leave_room",
  SEND_MESSAGE: "send_message",
  RECEIVE_MESSAGE: "receive_message",
  USER_JOINED: "user_joined",
  USER_LEFT: "user_left",
  ROOM_DATA: "room_data",
  TYPING_START: "typing_start",
  TYPING_STOP: "typing_stop",
  USER_TYPING: "user_typing",
  ERROR: "error",
});

export const LIMITS = Object.freeze({
  MIN_USERNAME_LENGTH: 2,
  MAX_USERNAME_LENGTH: 30,
  MIN_ROOM_LENGTH: 1,
  MAX_ROOM_LENGTH: 50,
  DEFAULT_MAX_MESSAGE_LENGTH: 2000,
  DEFAULT_MAX_ROOM_HISTORY: 100,
  DEFAULT_ROOM: "general",
});

export const SYSTEM_USER = Object.freeze({
  id: "system",
  username: "System",
});
