import os
import yaml

from settings import RESOURCES
from texts.resource_keys import ButtonText, MessageText

ResourceType = str | MessageText | ButtonText


class TextManager:
    def __init__(self) -> None:
        self.messages = self.load_messages()

    def get_text(self, key: ResourceType, lang: str | None = "ua") -> str | None:
        if str(key) in self.messages:
            return self.messages[str(key)][lang]
        else:
            raise ValueError(f"Key {key.name} not found")

    @staticmethod
    def load_messages() -> dict[str, dict[str, str]]:
        result = {}
        for type, path in RESOURCES.items():
            workdir = os.path.dirname(os.path.abspath(__file__))
            file_path = workdir + f"/{path}"
            with open(file_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for key, value in data.items():
                result[f"{type}.{key}"] = value
        return result


resource_manager = TextManager()


def text(key: ResourceType, lang: str | None = "ua") -> str | None:
    return resource_manager.get_text(key, lang)
