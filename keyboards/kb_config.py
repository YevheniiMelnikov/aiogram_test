from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ButtonConfig:
    text: str
    callback: Optional[str] = None
    url: Optional[str] = None
    row: int = 0


@dataclass
class KeyboardConfig:
    buttons: List[ButtonConfig] = field(default_factory=list)
    adjust_parameters: List[int] = field(default_factory=list)
