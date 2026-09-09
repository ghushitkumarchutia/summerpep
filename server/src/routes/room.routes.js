import { Router } from "express";
import {
  getActiveRooms,
  getRoomInfo,
  getMessageDetails,
  getThreadMessages,
} from "../controllers/room.controller.js";

const router = Router();

router.get("/", getActiveRooms);
router.get("/:room", getRoomInfo);
router.get("/:room/messages/:messageId", getMessageDetails);
router.get("/:room/messages/:messageId/thread", getThreadMessages);

export default router;
