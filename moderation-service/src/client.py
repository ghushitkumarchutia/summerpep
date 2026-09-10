import requests
from .config import CHAT_SERVER_URL

def fetch_room_metadata(room_name: str):
    url = f"{CHAT_SERVER_URL}/api/rooms/{room_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def dispatch_webhook_alert(webhook_url: str, payload: dict):
    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200
