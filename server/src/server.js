import { createServer } from "node:http";
import app from "./app.js";
import { env } from "./config/environment.js";
import { initializeSocket } from "./socket/index.js";

const server = createServer(app);
const io = initializeSocket(server);

const shutdown = () => {
  io.close(() => {
    server.close(() => {
      process.exit(0);
    });
  });

  setTimeout(() => {
    process.exit(1);
  }, 10000).unref();
};

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);

process.on("uncaughtException", (error) => {
  console.error("Uncaught Exception:", error.message);
  shutdown();
});

process.on("unhandledRejection", (reason) => {
  console.error("Unhandled Rejection:", reason);
  shutdown();
});

server.listen(env.PORT, () => {
  console.log(`Server listening on port ${env.PORT} in ${env.NODE_ENV} mode`);
});
