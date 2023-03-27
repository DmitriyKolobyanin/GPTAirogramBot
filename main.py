from os import getenv

import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

openai.api_key = getenv("API_CHAT_GPT")
bot = Bot(token=getenv("API_AIOGRAM"))
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот, который может с вами общаться на различные темы. Просто напишите мне что-то, "
                         "и я постараюсь ответить вам наилучшим образом.")


@dp.message_handler()
async def message_handler(message: types.Message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=1024,
        temperature=0.5,
    )
    await message.answer(response.choices[0].text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
