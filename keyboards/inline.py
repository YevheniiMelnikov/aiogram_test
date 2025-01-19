from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.kb_builder import KbBuilder
from keyboards.kb_config import ButtonConfig, KeyboardConfig
from texts.resource_keys import ButtonText as Btn
from texts.text_manager import text


def kb_v1() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    button1 = InlineKeyboardButton(
        text=text(Btn.test_button),
        callback_data="callback1"
    )
    button2 = InlineKeyboardButton(
        text=text(Btn.test_button2),
        callback_data="callback2"
    )
    button3 = InlineKeyboardButton(
        text=text(Btn.test_button3),
        url="https://google.com"
    )
    builder.row(button1, button2, button3)

    button4 = InlineKeyboardButton(
        text=text(Btn.test_button4),
        callback_data="callback4"
    )
    button5 = InlineKeyboardButton(
        text=text(Btn.test_button4),
        callback_data="callback5",
        url="https://example.com"
    )
    builder.row(button4, button5)

    return builder.as_markup()

def kb_v2(lang: str) -> InlineKeyboardMarkup:
    buttons = [
        ButtonConfig(text=text(Btn.test_button, lang), callback="callback1", row=0),
        ButtonConfig(text=text(Btn.test_button2, lang), callback="callback2", row=0),
        ButtonConfig(text=text(Btn.test_button3, lang), url="https://google.com", row=0),
        ButtonConfig(text=text(Btn.test_button4, lang), callback="callback4", row=1),
        ButtonConfig(text=text(Btn.test_button5, lang), callback="callback5", url="https://example.com", row=1),
    ]

    keyboard_config = KeyboardConfig(buttons)
    return KbBuilder(keyboard_config).build()
