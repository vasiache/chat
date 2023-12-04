import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

open_ai_token = ""
tg_token=""
openai.api_key=open_ai_token
bot=Bot(tg_token)
dp=Dispatcher(bot)

#chat
#@dp.message_handler()
#async def send(message : types.Message):
#    response = openai.Completion.create(
#    model="text-davinci-002",
#    prompt=message.text,
#    temperature=0.9,
#    max_tokens=1000,
#    top_p=1,
#    frequency_penalty=0.0,
#    presence_penalty=0.6,
#    stop=["You"])
#    await message.answer(response['choices'][0]['text'])

@dp.message_handler()
async def send(message : types.Message):
  #    if  '/ai' in message.text:
  bot.send_message(message.from_user.id, "Понял, ща")
  message.text=message.text[6:]
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.3,
    max_tokens=2000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6)
  
  await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
