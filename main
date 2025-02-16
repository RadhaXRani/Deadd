from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import start_handler
from handlers.download import download_handler
from handlers.inline import inline_query_handler

bot = Client(
    "YouTubeDownloaderBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot.add_handler(start_handler)
bot.add_handler(download_handler)
bot.add_handler(inline_query_handler)


from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running..."

def run():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    import os
    os.makedirs("downloads", exist_ok=True)  # Ensure downloads folder exists
    t = Thread(target=run)
    t.start()
    bot.run()

