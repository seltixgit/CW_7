import requests
from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(text, chat_id):
    params = {
        "text": text,
        "chat_id": chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
