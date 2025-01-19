from enum import Enum, auto


class ButtonText(Enum):
    test_button = auto()
    test_button2 = auto()
    test_button3 = auto()
    test_button4 = auto()
    test_button5 = auto()

    def __str__(self) -> str:
        return f"buttons.{self.name}"


class MessageText(Enum):
    start = auto()
    start2 = auto()
    start3 = auto()
    start4 = auto()
    start5 = auto()

    def __str__(self) -> str:
        return f"messages.{self.name}"
