from typing import Dict, List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class Item:
    item_name: str
    item_class: str
    item_type: str
    shop: str
    price: int
    image: str | None


@dataclass_json
@dataclass(frozen=True)
class Profile:
    profile_name: str
    owned_items: List[str]


@dataclass_json
@dataclass(frozen=True)
class DatabaseModel:
    items: Dict[str, Item] | None
    profiles: Dict[str, Profile] | None


default_database = {
    "items": None,
    "profiles": None
}
