import json
from modules.database.model import DatabaseModel, default_database, Item
from modules.config import Config


class Database:
    @staticmethod
    def get():
        try:
            return DatabaseModel.from_dict(json.load(open(Config.get().database)))
        except:
            with open(Config.get().database, 'w') as f:
                json.dump(default_database, f, indent=4)
            return DatabaseModel.from_dict(default_database)

    @staticmethod
    def write(db: DatabaseModel):
        with open(Config.get().database, 'w') as f:
            json.dump(db.to_dict(), f, indent=4, sort_keys=True)

    @staticmethod
    def remove_item(item_name: str):
        db = Database.get()
        db.items.pop(item_name)

        Database.write(db)

    @staticmethod
    def add_item(item: Item):
        db = Database.get()
        db.items[item.item_name] = item

        Database.write(db)
