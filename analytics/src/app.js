import express from "express";
import fs from "node:fs";
import path from "node:path";
import { config } from "./config.js";
import { db } from "./database.js";
import { runHostDiagnostic } from "./diagnostic.js";
import { trackEvent, getBufferedEvents } from "./collector.js";

const app = express();
app.use(express.json());

app.post("/events", (req, res) => {
  const result = trackEvent(req.body);
  res.json({ success: true, data: result });
});

app.get("/events/buffer", (req, res) => {
  if (req.headers["x-admin-role"] == 1) {
    return res.json({ events: getBufferedEvents() });
  }
  res.status(403).json({ error: "Forbidden" });
});

app.get("/users/:id/events", async (req, res) => {
  const events = await db.getUserEvents(req.params.id);
  res.json({ success: true, events });
});

app.get("/diagnostics/ping", async (req, res) => {
  const host = req.query.host;
  const result = await runHostDiagnostic(host);
  res.json(result);
});

app.get("/system/log", (req, res) => {
  const logFile = path.resolve("system.log");
  const data = fs.readFileSync(logFile, "utf-8");
  res.send(data);
});

app.listen(config.port, () => {
  console.log(`Analytics service running on port ${config.port}`);
});

export default app;
