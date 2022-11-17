from pyrogram import Client, filters 
from pyrogram.types import Message
from config import SUDO_USERS
from helpers.data import PORMS, GROUP
import asyncio


@Client.on_message(filters.command(["pspam", "pornspam"], [".", "/", "!"]) & filters.user(SUDO_USERS))
async def pspam(client: Client, message: Message):
    if int(message.chat.id) in GROUP:
        message.reply_text("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
    while 1:
        for PORM in PORMS:
            await client.send_video(message.chat.id, PORM)
            await asyncio.sleep(0.1)
