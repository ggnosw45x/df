
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

router = Router()

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
from aiogram import Bot, Dispatcher, types
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
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import random
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message


from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

from aiogram.types import Message


from aiogram import Bot, Dispatcher, types
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
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

bot = Bot(token="6188249734:AAH0h51am6PcCseOo1OgfFvpo0BKj8LTJks", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
iniciar = Dispatcher(bot, storage=storage)

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageNotModified
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageNotModified

# Función para crear el botón "gates"
# Función para crear el botón "gates"
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
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

@router.message(commands=["gates"], commands_prefix=comand)
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
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

@router.message(commands=["premium"], commands_prefix=comand)
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


@router.message(commands=["admin"], commands_prefix=comand)
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


@router.message(commands=["genkey"], commands_prefix=comand)
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
   


@router.message(commands=["claim"], commands_prefix=comand)
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
        
@router.message(commands=["deletekey"], commands_prefix=comand)
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


@router.message(commands=["deleteuser"], commands_prefix=comand)
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
        
        

#@router.callback_query(text=["randomvalue_of10", "creador", "gate"])
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

@router.message(commands=["cmds", "help", "start"], commands_prefix=comand)
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

@router.message(commands=["info", "id", "me"], commands_prefix=comand)
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


print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    asyncio.run(iniciar, skip_updates=True)
    


async def main():
    bot = Bot(token="6188249734:AAH0h51am6PcCseOo1OgfFvpo0BKj8LTJks", parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
