
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Fiqhiy savol")],
        [
            KeyboardButton(text="💧 Tahorat"),
            KeyboardButton(text="🕌 Namoz va ro‘za"),
        ],
        [KeyboardButton(text="📚 Fiqh kitoblari")],
    ],
    resize_keyboard=True,
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum!\n\n"
        "📚 Hanafiy Fiqhi Ensiklopediyasiga xush kelibsiz.\n\n"
        "Hozirda bot tayyorlanmoqda. "
        "Fiqhiy ma’lumotlar keyingi bosqichda qo‘shiladi.",
        reply_markup=menu,
    )

@dp.message(F.text.in_([
    "🔎 Fiqhiy savol",
    "💧 Tahorat",
    "🕌 Namoz va ro‘za",
    "📚 Fiqh kitoblari",
]))
async def coming_soon(message: Message):
    await message.answer(
        "⏳ Ushbu bo‘lim hozirda tayyorlanmoqda.\n\n"
        "Hanafiy fiqhiga oid ma’lumotlar "
        "manbalar tekshirilganidan keyin qo‘shiladi."
    )

async def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN sozlanmagan!")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
