from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types



bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    with open('./images/2.png', 'rb') as photo:
        await message.answer_photo(photo, caption="Используйте команду /waifu, чтобы сгенерировать картинку")


@dp.message_handler(commands=['waifu'])
async def waifu(message: types.Message):
    with open('./images/1.png', 'rb') as photo:
        await message.answer_photo(photo, caption="Напишите любой текст (на английском, указывая параметры через запятую.\nНапример: looking at viewer, masterpiece, best quality, bright hair, blue eyes, outdoors\nМетодичка по параметрам: /prompts")


@dp.message_handler()
async def echo(message: types.Message):
    with open('./images/0.png', 'rb') as photo:
        await message.reply_photo(photo, caption='Waifu')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

