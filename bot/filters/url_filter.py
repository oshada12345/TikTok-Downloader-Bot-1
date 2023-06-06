from aiogram.filters import BaseFilter
from aiogram.types import Message



class UrlFilter(BaseFilter):
    """Url Filter."""
    async def __call__(self, message: Message) -> bool:
        if message.text.startswith("https://www.tiktok.com/") \
        or message.text.startswith("https://vt.tiktok.com/"):
            return True
        
        await message.answer('[🏖 TikTok Download API 🏖](https://github.com/Single-Developers/API/blob/main/tiktok/Note.md)\n\n[🔥 SL Developers </> 🇱🇰](https://t.me/SL_Developers)'),
        await message.reply_sticker('CAACAgUAAxkBAAED9kRiDq_GkOHuRHPeVv4IRhsvy4NtbwACqQQAAncUyFftN80YUiyXnyME')

        return False
        
