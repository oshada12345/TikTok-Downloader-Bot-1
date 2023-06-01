import os

from aiogram import Router, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import CancelState, TimedStorage, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.ext import keyboards, GetUrl, TikTok
from bot.filters import UrlFilter, CancelFilter

router = Router(name="General Handler")


class VideoState(StatesGroup):
    Waiting = State()


async def get_url(message: Message) -> None:
    await message.answer(
        "⏱ Ｗａｉｔ．．．🧬          ▰▰▰▰▰▰▰▰▱▱ 80%",
        reply_markup=keyboards.KeyboardRemove()
    )

    try:
        tik_tok = TikTok(message.text)

        video = tik_tok.download_video(f"{message.from_user.username}.mp4")
        aiovideo = FSInputFile(video)

        await message.answer_video(video=aiovideo)
        os.remove(video)

    except Exception:
        await message.answer("🎶🎶 Ｔｈｅ ＵＲＬ ｉｓ ｎｏｔ ｃｏｒｒｅｃｔ．✔️ ✔️ ")


@router.message(GetUrl.url, CancelFilter(), UrlFilter())
async def get_url_fsm(message: Message, state: FSMContext) -> None:
    await state.update_data(url=message.text)
    await state.clear()

    await get_url(message)


@router.message(UrlFilter())
async def get_url_filter(message: Message) -> None:
    await get_url(message)


@router.callback_query("share_video")
async def share_video(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    video_url = data.get("video_url")

    if video_url:
        await callback_query.message.answer_video(video_url)
    else:
        await callback_query.message.answer("No video available to share.")

    await callback_query.answer()


async def send_video_with_share_button(message: Message) -> None:
    await message.answer(
        "⏱ Ｗａｉｔ．．．🧬          ▰▰▰▰▰▰▰▰▱▱ 80%",
        reply_markup=keyboards.KeyboardRemove()
    )

    try:
        tik_tok = TikTok(message.text)

        video = tik_tok.download_video(f"{message.from_user.username}.mp4")
        aiovideo = FSInputFile(video)

        await message.answer_video(
            video=aiovideo,
            reply_markup=types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton(
                    text="Share Video",
                    callback_data="share_video"
                )
            )
        )
        os.remove(video)

    except Exception:
        await message.answer("🎶🎶 Ｔｈｅ ＵＲＬ ｉｓ ｎｏｔ ｃｏｒｒｅｃｔ．✔️ ✔️ ")


@router.message(GetUrl.url, CancelFilter(), UrlFilter())
async def send_video_with_share_button_fsm(message: Message, state: FSMContext) -> None:
    await state.update_data(url=message.text)
    await state.clear()

    await send_video_with_share_button(message)


@router.message(UrlFilter())
async def send_video_with_share_button_filter(message: Message) -> None:
    await send_video_with_share_button(message)
