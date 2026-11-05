import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_senal(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }
    requests.post(url, data=datos)

enviar_senal("🤖 Bot OTC conectado. Esperando señales.")# Bot-de-senales-otc
