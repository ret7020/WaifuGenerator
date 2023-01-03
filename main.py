from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
import random
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import transformers

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

print("[DEBUG] Loading model")
pipe = StableDiffusionPipeline.from_pretrained(
    'hakurei/waifu-diffusion',
    torch_dtype=torch.float32
).to('cuda')


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
  prompt = "looking at viewer, masterpiece, best quality, bright hair, blue eyes, medium boobs in mini skirt, indoors, popular, beautiful"

  # Bypass NSFW checker :)
  # Only for work; freelance yepta

  def dummy(images, **kwargs):
      return images, False
  pipe.safety_checker = dummy

  with autocast("cuda"):
      image = pipe(prompt, guidance_scale=6).images[0]
  file_id = random.randint(10000, 10000000)
  image.save(f"./tmp_gen/{file_id}.png")

  with open(f'./tmp_gen/{file_id}.png', 'rb') as photo:
      await message.reply_photo(photo, caption='Generated waifu image')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

