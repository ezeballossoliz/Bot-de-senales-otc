import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("Falta configurar TELEGRAM_TOKEN")

URL = f"https://api.telegram.org/bot{TOKEN}/"

def enviar_mensaje(chat_id, mensaje):
    requests.post(
        URL + "sendMessage",
        data={"chat_id": chat_id, "text": mensaje}
    )

def iniciar_bot():
    ultimo_id = 0

    print("Bot de Telegram iniciado")

    while True:
        try:
            respuesta = requests.get(
                URL + "getUpdates",
                params={
                    "offset": ultimo_id + 1,
                    "timeout": 30
                },
                timeout=35
            ).json()

            for update in respuesta.get("result", []):
                ultimo_id = update["update_id"]

                mensaje = update.get("message", {})
                chat_id = mensaje.get("chat", {}).get("id")
                texto = mensaje.get("text", "")

                if not chat_id:
                    continue

                if texto == "/start":
                    enviar_mensaje(
                        chat_id,
                        "¡Bienvenido a Mi Polarium Signals OTC!\n\n"
                        "Comandos disponibles:\n"
                        "/senal - Consultar estado\n"
                        "/ayuda - Ver ayuda"
                    )

                elif texto == "/senal":
                    enviar_mensaje(
                        chat_id,
                        "Sistema OTC en preparación.\n"
                        "Todavía no hay señales verificadas. "
                        "No operes basándote en señales de prueba."
                    )

                elif texto == "/ayuda":
                    enviar_mensaje(
                        chat_id,
                        "Este bot está en desarrollo para análisis OTC."
                    )

        except Exception as error:
            print("Error:", error)
            time.sleep(5)

if __name__ == "__main__":
    iniciar_bot()
