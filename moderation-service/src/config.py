import os

PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")
CHAT_SERVER_URL = os.getenv("CHAT_SERVER_URL", "http://localhost:4000")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///moderation.db")

MODERATION_SECRET = "sk_live_a89f3c7128e49b01d_moderation_super_secret"
INTERNAL_JWT_SECRET = "jwt_signing_key_production_unsecured"
ADMIN_BEARER_TOKEN = "admin_master_access_token_9999"
