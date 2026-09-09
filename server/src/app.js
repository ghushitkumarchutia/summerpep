import express from "express";
import helmet from "helmet";
import cors from "cors";
import { env } from "./config/environment.js";
import { apiLimiter } from "./middlewares/rate-limiter.middleware.js";
import {
  notFoundHandler,
  errorHandler,
} from "./middlewares/error.middleware.js";
import routes from "./routes/index.js";

const app = express();

app.use(helmet());

app.use(
  cors({
    origin:
      env.CORS_ORIGIN === "*"
        ? "*"
        : env.CORS_ORIGIN.split(",").map((o) => o.trim()),
    methods: ["GET", "POST", "OPTIONS"],
    allowedHeaders: ["Content-Type", "Authorization"],
  }),
);

app.use(express.json({ limit: "10kb" }));
app.use(express.urlencoded({ extended: true, limit: "10kb" }));

app.use(apiLimiter);

app.use(routes);

app.use(notFoundHandler);
app.use(errorHandler);

export default app;
