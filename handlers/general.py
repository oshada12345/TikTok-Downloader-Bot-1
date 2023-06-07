from telegram import ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
import os

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.ext import keyboards, GetUrl, TikTok
from bot.filters import UrlFilter, CancelFilter


# ParseMode Type For All Messages
_ParseMode=ParseMode.MARKDOWN

router = Router(name="General Handler")




async def get_url(message: Message) -> None:
    await message.reply_sticker('CAACAgIAAxkBAAEB2MNkfrAJYL0I9YHrJLPr3RPgj7SQbAACKBsAApXE8Eo3HwK46IRtPy8E')
    await message.answer(
        "🚀 DOᗯᑎᒪOᗩᗪIᑎG Video TO Sᕮᖇᐯᕮᖇ ....",
        reply_markup=keyboards.KeyboardRemove()
    )
     

    try:
        tik_tok = TikTok(message.text)

        video = tik_tok.download_video(f"{message.from_user.username}.mp4")
        aiovideo = FSInputFile(video)

        await message.answer_video(video=aiovideo)
        os.remove(video) 
        
          # Get the video caption
        caption = tik_tok.get_video_caption("fk")

        await message.answer_video(video=aiovideo, caption=caption)
        os.remove(video)

    except Exception:
        await message.answer('[🏖 TikTok Download API 🏖](https://github.com/Single-Developers/API/blob/main/tiktok/Note.md)\n\n[🔥 SL Developers </> 🇱🇰](https://t.me/SL_Developers)',parse_mode=_ParseMode)
          



@router.message(GetUrl.url, CancelFilter(), UrlFilter())
async def get_url_fsm(message: Message, state: FSMContext) -> None:
    await state.update_data(url=message.text)
    await state.clear()

    await get_url(message)

@router.message(UrlFilter())
async def get_url_filter(message: Message) -> None:
    await get_url(message)
