from pyrogram import Client, filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNELS

async def check_force_sub(client, message):
    for channel in FORCE_SUB_CHANNELS:
        try:
            user_status = await client.get_chat_member(channel, message.from_user.id)
            if user_status.status in ["kicked", "left"]:
                await message.reply(f"कृपया इस चैनल को जॉइन करें: {channel}")
                return False
        except:
            await message.reply("कोई समस्या है! कृपया बाद में प्रयास करें।")
            return False
    return True

async def start(client, message: Message):
    if not await check_force_sub(client, message):
        return
    await message.reply("स्वागत है! YouTube ऑडियो, वीडियो और प्लेलिस्ट डाउनलोड करने के लिए लिंक भेजें या Inline Mode का उपयोग करें।")

start_handler = filters.command("start")(start)
