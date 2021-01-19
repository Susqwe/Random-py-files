from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from telegraphapi import Telegraph


ADMIN_ID = 111111
TOKEN = "1111111:XXxxXXxXxxXxXxXxXXxXxXXxXX"


storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


def tgraph():
	telegraph = Telegraph()
	telegraph.createAccount("Your dream")
	a = ""
	with open('users.txt', 'r', encoding='utf-8') as f:
		for l in f:
			a = a + str(l)
	page = telegraph.createPage("Список пользователей.", html_content="<p>" + a + "<p>")
	return 'http://telegra.ph/{}'.format(page['path'])
	
	
but1 = 'Добавить пользователя'
but2 = 'Вывести список'


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup.add(but1)
markup.add(but2)


markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup2.add(but2)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	if message['from']['id'] == ADMIN_ID:
		await message.reply(f"Привет, выбери действие.", reply_markup=markup, reply=False)
	else:
		await message.reply(f"Привет, выбери действие.", reply_markup=markup2)


@dp.message_handler(text='Вывести список')
async def cmd_start(message: types.Message):
	link = tgraph()
	await message.reply('Вот доступные пользователи: ' + link.replace('telegra.ph', 'tgraph.io'), reply=False)


@dp.message_handler(commands=['users'])
async def process_start_command(message: types.Message):
	link = tgraph()
	await message.reply('Вот доступные пользователи: ' + link.replace('telegra.ph', 'tgraph.io'), reply=False)


class kod_key(StatesGroup):
    word = State()
    crypted = State()


@dp.message_handler(text='Добавить пользователя')
async def cmd_start(message: types.Message):
	if message['from']['id'] == ADMIN_ID:
		await kod_key.word.set()
		await message.reply('Введи username\nПример: @username', reply=False)


@dp.message_handler(state=kod_key.word)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['word'] = message.text
    await message.reply('Введи город\nПример: Рим', reply=False)
    await kod_key.next()


@dp.message_handler(state=kod_key.crypted)
async def process_age(message: types.Message, state: FSMContext):
	await state.update_data(crypted=message.text)
	async with state.proxy() as data:
		with open("users.txt", 'a', encoding='utf-8') as f:
			f.write(data['word'] + " " + data["crypted"] + "\n")
	await message.reply(f'Пользователь успешно записан в файл.\nUsername: ' + data['word'] + ' \nГород: ' + data['crypted'], reply=False)
	await state.finish()



if __name__ == '__main__':
    print("starting")
    executor.start_polling(dp)