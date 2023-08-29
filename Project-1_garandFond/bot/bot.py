#files
from constants.constants import Constants
from constants.localization.message import Message
from constants.localization.keyboard import Keyboard
#lib
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup
#initialize
bot = Bot(Constants.getToken())
dp = Dispatcher(bot=bot)
#keyboard
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add(Keyboard.increase).add(Keyboard.decrease)

counter = InlineKeyboardMarkup(row_width=2)
counter.add(InlineKeyboardMarkup("-1"),InlineKeyboardMarkup("+1"))
#hendler - start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.message):
    await message.answer(Message.hello(),reply_markup=counter)
#hendler - error for message
@dp.message_handler()
async def cmd_error(message: types.message):
    await message.reply(Message.error())


if __name__ == '__main__':
    executor.start_polling(dp)

 