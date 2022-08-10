from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_dp
#Клиентская часть

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id,'Приятного аппетита', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_Sheef1337Bot')

#@dp.message_handler(commands=[Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id,
	 'Пн - Пт с 9:00 до 18:00.')

#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Россия, Саратов, микрорайон Октябрьский, 8-я линия, 54.')

#@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
	await sqlite_dp.sql_read(message)

#@dp.message_handler(commands=['Прайс'])
async def giper_ssilka(message : types.Message):
	await bot.send_message(message.from_user.id, 'https://xn--n1aacmla.xn--p1ai/mprices/')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение'])
	dp.register_message_handler(pizza_menu_command, commands=['Меню'])
	dp.register_message_handler(giper_ssilka,commands=['Прайс'])