from aiogram.filters import BaseFilter
from aiogram.types import Message


(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 :) 𝖧𝗂𝗍 /start \n\n𝖧𝗂𝗍 /help 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉 ;)\n\n\n𝖧𝗂𝗍 /ping 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝗂𝗇𝗀 😁")


class UrlFilter(BaseFilter):
    """Url Filter."""
    async def __call__(self, message: Message) -> bool:
        if message.text.startswith("https://www.tiktok.com/") \
        or message.text.startswith("https://vt.tiktok.com/"):
            return True
        
        await message.answer('ᴘʟᴢ ꜱᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ'),
        await message.reply_sticker('CAACAgIAAxkBAAEB2NdkfxPhIiGJP1h5tmOFkuGkFI33KQACXhgAAogOKEhUGNKuQ9GUEC8E')

        return False
        
