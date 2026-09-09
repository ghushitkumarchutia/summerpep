import { Router } from "express";
import healthRoutes from "./health.routes.js";
import roomRoutes from "./room.routes.js";

const router = Router();

router.use("/health", healthRoutes);
router.use("/api/rooms", roomRoutes);

export default router;
