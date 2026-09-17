import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! 🚀\nЯ работаю в облаке 24/7!")

@dp.message()
async def echo_msg(message: types.Message):
    await message.answer(f"Ты написал: {message.text} 🔥")

async def main():
    print("Бот запущен в облаке!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
