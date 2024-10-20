from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio


API_TOKEN = "7784619603:AAEs2WaT4WUuag_x04cRcOfyOvC6JUq2IoU"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

my_router = Router(name=__name__)

@my_router.message(Command('start'))
async def start(message: types.Message):
    print("Мы получили сообщение:", message.text)
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@my_router.message()
async def all_message(message: types.Message):
    print("Мы получили сообщение:", message.text)
    await message.answer('Введите команду /start, чтобы начать общение.')

dp.include_router(my_router)

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())