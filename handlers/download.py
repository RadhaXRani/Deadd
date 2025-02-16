from pyrogram import Client, filters
from pyrogram.types import Message
from utils.youtube import download_youtube
from utils.auth import is_paid_user
from config import FREE_PLAN

async def download(client, message: Message):
    user_id = message.from_user.id
    url = message.text

    if not url.startswith("http"):
        await message.reply("कृपया एक वैध YouTube लिंक भेजें।")
        return

    is_paid = is_paid_user(user_id)
    if is_paid:
        await message.reply("ऑडियो, वीडियो, या प्लेलिस्ट डाउनलोड हो रहा है...")
        await download_youtube(client, message, url, "full")
    else:
        await message.reply("केवल ऑडियो डाउनलोड हो रहा है...")
        await download_youtube(client, message, url, FREE_PLAN["downloads"])

download_handler = filters.text & ~filters.command("start")(download)
