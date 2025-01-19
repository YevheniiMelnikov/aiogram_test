from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from collections import defaultdict

from keyboards.kb_config import KeyboardConfig


class KbBuilder:
    def __init__(self, config: KeyboardConfig):
        self.config = config
        self.builder = InlineKeyboardBuilder()

    def build(self) -> InlineKeyboardMarkup:
        rows = defaultdict(list)
        for button in self.config.buttons:
            rows[button.row].append(
                InlineKeyboardButton(text=button.text, callback_data=button.callback, url=button.url)
            )

        for row_num in sorted(rows.keys()):
            self.builder.row(*rows[row_num])

        if self.config.adjust_parameters:
            self.builder.adjust(*self.config.adjust_parameters)

        return self.builder.as_markup()
