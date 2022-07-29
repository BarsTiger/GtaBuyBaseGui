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
    image: str


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


aa = DatabaseModel.from_dict(
    {
        "items": {
            "sieg": {
                "item_name": "seig",
                "item_class": "meow",
                "item_type": "bebra44ka",
                "shop": "aaaaaaatb",
                "price": 100000000,
                "image": "https://magichitler.sieg/public/static/img/mama.png"
            },
            "aaaaaaaaaaaaa": {
                "item_name": "aaaaaaaaaaaaa",
                "item_class": "aaaaaaaaaaaaaaaaaaaa",
                "item_type": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "shop": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "price": 10000000000000000,
                "image": "https://sieg-heil.com/"
            }
        },
        "profiles": {
            "BarsTiger": {
                "profile_name": "BarsTiger",
                "owned_items": [
                    "aaaaaaaaaaaaa"
                ]
            }
        }
    }
)
