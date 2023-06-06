from aiogram.filters import BaseFilter
from aiogram.types import Message



class UrlFilter(BaseFilter):
    """Url Filter."""
    async def __call__(self, message: Message) -> bool:
        if message.text.startswith("https://www.tiktok.com/") \
        or message.text.startswith("https://vt.tiktok.com/"):
            return True
        
        await message.answer('💀👹  ώέ𝕃ⒸỖｍ𝐞 т๏ 𝔱Ⓘк 𝔱ØＫ 𝓭𝓞Ŵｎ𝔩σ卂𝕕𝕖𝓡 𝐛𝕆Ⓣ  🔥☆/n/nᴘʟᴢ ꜱᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ'),
        await message.reply_sticker('CAACAgUAAxkBAAED9kRiDq_GkOHuRHPeVv4IRhsvy4NtbwACqQQAAncUyFftN80YUiyXnyME')

        return False
        
