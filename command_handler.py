from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards import inline as kb
from models import User
from texts.resource_keys import MessageText
from texts.text_manager import text

command_router = Router()


@command_router.message(Command('start'))
async def say_hi(message: Message):
    await message.answer(text(MessageText.start))
    await message.answer("Test with the following commands:\n/kb1\n/kb2")


@command_router.message(Command('kb1'))
async def build_keyboard_1(message: Message):
    await message.answer("Keyboard v1", reply_markup=kb.kb_v1())


@command_router.message(Command('kb2'))
async def build_keyboard_2(message: Message):
    user = User(1, "username", "ua")
    await message.answer("Keyboard v2", reply_markup=kb.kb_v2(user.lang))  # pass the lang here
