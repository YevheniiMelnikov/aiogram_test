from contextlib import suppress

from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import country_keyboard, alphabet_keyboard
from keyboards.countries import COUNTRIES
from logger import logger

main_router = Router()


@main_router.callback_query(F.data.startswith("letter:"))
async def process_letter(callback_query: CallbackQuery):
    letter = callback_query.data.split(":")[1]
    countries = [c for c in COUNTRIES if c["name"].startswith(letter)]
    await callback_query.message.edit_text(
        f"Виберіть країну:",
        reply_markup=country_keyboard(countries, page=0, letter=letter)
    )

@main_router.callback_query(F.data.startswith("page:"))
async def paginate_countries(callback_query: CallbackQuery):
    data = callback_query.data.split(":")
    page = int(data[1])
    letter = data[2]
    countries = [c for c in COUNTRIES if c["name"].startswith(letter)]
    await callback_query.message.edit_reply_markup(reply_markup=country_keyboard(countries, page, letter))

@main_router.callback_query(F.data.startswith("country:"))
async def process_country(callback_query: CallbackQuery, state: FSMContext):
    country_name = callback_query.data.split(":")[1]
    country = next(c for c in COUNTRIES if c["name"] == country_name)
    await state.update_data(time_zone=country["time_zone"])
    await callback_query.answer("Збрежено")
    logger.info(f"Country: {country_name}, Time zone: {country['time_zone']}")
    await callback_query.message.delete()


@main_router.callback_query(F.data == "back")
async def go_back_to_alphabet(callback_query: CallbackQuery):
    with suppress(TelegramBadRequest):
        await callback_query.message.edit_text(
            "Виберіть букву, на яку починається назва країни:",
            reply_markup=alphabet_keyboard()
        )
