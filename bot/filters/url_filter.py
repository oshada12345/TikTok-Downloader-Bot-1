from aiogram.filters import BaseFilter
from aiogram.types import Message



class UrlFilter(BaseFilter):
    """Url Filter."""
    async def __call__(self, message: Message) -> bool:
        if message.text.startswith("https://www.tiktok.com/") \
        or message.text.startswith("https://vt.tiktok.com/"):
            return True
        
        await message.answer(' 🔥☆ ᴘʟᴢ ꜱᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ \n\n\n @Satan666661'),
        await message.reply_sticker('CAACAgIAAxkBAAEB2Ltkfq8OzEjD30sLd8EKCaDkPQ112AACBAEAAladvQreBNF6Zmb3bC8E')

        return False
        
