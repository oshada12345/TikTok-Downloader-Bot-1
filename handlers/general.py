import os

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.ext import keyboards, GetUrl, TikTok
from bot.filters import UrlFilter, CancelFilter


router = Router(name="General Handler")



async def get_url(message: Message,sticker: Sticker) -> None:
    await message.reply_sticker('CAACAgUAAxkBAAEB2K9kfq2J_cOk-k-uAlMsw0UhQkn-bgACawYAAuWrKVW_hr19UXvxkS8E'),
    await message.answer(
        "🚀 DOᗯᑎᒪOᗩᗪIᑎG Video TO Sᕮᖇᐯᕮᖇ ....",
        reply_markup=keyboards.KeyboardRemove()
    ),
     

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
