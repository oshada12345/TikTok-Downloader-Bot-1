import os

from aiogram import Router
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.ext import keyboards, GetUrl, TikTok
from bot.filters import UrlFilter, CancelFilter


router = Router(name="General Handler")

async def get_url(message: Message) -> None:
    await message.reply_sticker('CAACAgIAAxkBAAEB2MNkfrAJYL0I9YHrJLPr3RPgj7SQbAACKBsAApXE8Eo3HwK46IRtPy8E')
    await message.answer(
        "🚀 DOWNLOADING VIDEO TO SERVER ....",
        reply_markup=keyboards.KeyboardRemove()
    )

    try:
        tik_tok = TikTok(message.text)

        video = tik_tok.download_video(f"{message.from_user.username}.mp4")
        aiovideo = FSInputFile(video)

        # Get the video caption
        caption = tik_tok.get_video_caption()

        share_button = InlineKeyboardButton("Share", switch_inline_query=f"{caption}")
        reply_markup = InlineKeyboardMarkup([[share_button]])

        await message.answer_video(video=aiovideo, caption=caption, reply_markup=reply_markup)
        os.remove(video)

    except Exception:
        await message.reply("🎶🎶 The URL is not correct. ✔️ ✔️ ")


@router.message(GetUrl.url, CancelFilter(), UrlFilter())
async def get_url_fsm(message: Message, state: FSMContext) -> None:
    await state.update_data(url=message.text)
    await state.clear()

    await get_url(message)


@router.message(UrlFilter())
async def get_url_filter(message: Message) -> None:
    await get_url(message)
