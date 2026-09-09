import { Router } from "express";
import { getActiveRooms, getRoomInfo } from "../controllers/room.controller.js";

const router = Router();

router.get("/", getActiveRooms);
router.get("/:room", getRoomInfo);

export default router;
