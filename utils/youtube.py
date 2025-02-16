import yt_dlp
from pyrogram import Client
from pyrogram.types import Message

async def download_youtube(client, message, url, download_type):
    ydl_opts = {
        "format": "bestaudio" if download_type == "audio" else "best",
        "outtmpl": "downloads/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        ydl.download([url])
        title = info.get("title", "डाउनलोड हो गया")
        await message.reply(f"{title} डाउनलोड हो गया!")
