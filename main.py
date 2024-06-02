import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard
from randomfox import fox


#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Hi, {message.from_user.full_name}!', reply_markup=keyboard)


@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'bye, {message.chat.first_name}!')


@dp.message(Command(commands=['info']))
@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Hello, your number is: {number}!')

@dp.message(lambda message: 'show fox' in message.text.lower())
async def show_fox(message: types.Message):
    print(f"Received message: {message.text}")
    img_fox = fox()
    await message.answer('Here is your fox')
    await message.answer_photo(img_fox)



@dp.message(F.text)
async def msg(message: types.Message):
    if 'Hi' in message.text.lower():
        await message.reply('Hello!')
    elif 'How are you' in message.text.lower():
        await message.reply('I am fine and you')
    else:
        await message.reply('I didnt get you...')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


