from aiogram import Bot, Dispatcher, executor, types
import logging
import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("سلام! لینک مورد نظر خود را ارسال کنید.\n\n📥 دانلود از:\n📌 یوتیوب\n📌 اینستاگرام\n📌 تیک‌تاک")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
