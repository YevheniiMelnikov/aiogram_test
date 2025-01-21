from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.inline import alphabet_keyboard


command_router = Router()


@command_router.message(Command('start'))
async def say_hi(message: Message):
    await message.answer("Виберіть букву, на яку починається назва країни:", reply_markup=alphabet_keyboard())
