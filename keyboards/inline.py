from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def country_keyboard(countries: list[dict], page: int, letter: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    start = page * 8
    end = start + 8
    country_slice = countries[start:end]

    builder.add(*(InlineKeyboardButton(
        text=country["name"],
        callback_data=f"country:{country['name']}"
    ) for country in country_slice))
    builder.adjust(2)

    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton(
            text="←",
            callback_data=f"page:{page - 1}:{letter}"
        ))

    if len(countries) > end:
        navigation_buttons.append(InlineKeyboardButton(
            text="→",
            callback_data=f"page:{page + 1}:{letter}"
        ))

    if navigation_buttons:
        builder.row(*navigation_buttons)

    builder.row(InlineKeyboardButton(
        text="← Назад",
        callback_data="back"
    ))

    return builder.as_markup()


def alphabet_keyboard() -> InlineKeyboardMarkup:
    alphabet = [chr(i) for i in range(65, 91) if chr(i) != 'X']
    builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=letter, callback_data=f"letter:{letter}") for letter in alphabet]
    for i in range(0, len(buttons), 5):
        builder.row(*buttons[i:i+5])
    builder.row(InlineKeyboardButton(text="← Назад", callback_data="back"))
    return builder.as_markup()

# def kb_builder_example(lang: str) -> InlineKeyboardMarkup:
#     buttons = [
#         ButtonConfig(text=text(Btn.test_button, lang), callback="callback1", row=0),
#         ButtonConfig(text=text(Btn.test_button2, lang), callback="callback2", row=0),
#         ButtonConfig(text=text(Btn.test_button3, lang), url="https://google.com", row=0),
#         ButtonConfig(text=text(Btn.test_button4, lang), callback="callback4", row=1),
#         ButtonConfig(text=text(Btn.test_button5, lang), callback="callback5", url="https://example.com", row=1),
#     ]
#
#     keyboard_config = KeyboardConfig(buttons)
#     return KbBuilder(keyboard_config).build()
