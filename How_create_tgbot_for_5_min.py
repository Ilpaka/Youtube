import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "ВСТАВЬТЕ ВАШ API КЛЮЧ"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кнопка 1", callback_data = "btn1")],
    [InlineKeyboardButton(text="Кнопка 2", callback_data = "btn2")]
])

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=markup)

@dp.callback_query(lambda c: c.data == 'btn1')
async def process_btn1(callback_query):
    await callback_query.message.answer(f"{callback_query.from_user.full_name} нажал кнопку 1")

@dp.callback_query(lambda c: c.data == 'btn2')
async def process_btn1(callback_query):
    await callback_query.answer(f"{callback_query.from_user.full_name} нажал кнопку 2")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
