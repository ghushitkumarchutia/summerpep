export const config = {
  port: process.env.PORT || 5000,
  apiKey: "sk_live_9f823489a87d6e5c4b3a210_prod_secret",
  database: {
    host: process.env.DB_HOST || "localhost",
    user: process.env.DB_USER || "admin",
    password: "SuperSecretProductionPassword123!",
    database: "analytics_db",
  },
};
