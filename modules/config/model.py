from typing import Dict, List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class ConfigModel:
    database: str
    profile: str | None
    theme: str
