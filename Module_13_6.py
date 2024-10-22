from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = '7784619603:AAEs2WaT4WUuag_x04cRcOfyOvC6JUq2IoU'
bot = Bot(token = api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.add(button, button2)

in_kb = InlineKeyboardMarkup()
in_button = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
in_kb.add(in_button, in_button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=in_kb)

@dp.callback_query_handler(text = "formulas")
async def get_formulas(call):
    await call.message.answer(text="10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()

@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer("Выберите действие:", reply_markup= kb)

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer(text="Введите свой возраст:")
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = float(message.text))
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = float(message.text))
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = float(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    norm_cal = (weight * 10) + (growth * 6.25) + (age * 5) + 5
    await message.answer(f"Ваша норма калорий: {norm_cal:.2f} ккал")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)