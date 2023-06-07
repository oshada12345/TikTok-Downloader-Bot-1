from aiogram.filters import BaseFilter
from aiogram.types import Message



class UrlFilter(BaseFilter):
    """Url Filter."""
    async def __call__(self, message: Message) -> bool:
        if message.text.startswith("https://www.tiktok.com/") \
        or message.text.startswith("https://vt.tiktok.com/"):
            return True
        
        await message.answer('Please send me the video link !'),
        await message.reply_sticker('CAACAgUAAxkBAAEB2OdkgFIQIEMK9hXGKe7pa33VUZludAAC7QYAAivOgFSyWtJpGDd-Yi8E')

        return False
        
