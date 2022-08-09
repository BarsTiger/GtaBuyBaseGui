import json
from modules.database.model import DatabaseModel, default_database, Item, Profile
from modules.config import Config


class Database:
    @staticmethod
    def get():
        try:
            return DatabaseModel.from_dict(json.load(open(Config.get().database)))
        except Exception as e:
            print(f"Cannot load database: {e}. Writing default database")
            print("Old data:")
            print(open(Config.get().database).read())
            with open(Config.get().database, 'w') as f:
                json.dump(default_database, f, indent=4)
            return DatabaseModel.from_dict(default_database)

    @staticmethod
    def get_profile():
        return Database.get().profiles[Config.get().profile]

    @staticmethod
    def write(db: DatabaseModel):
        with open(Config.get().database, 'w') as f:
            json.dump(db.to_dict(), f, indent=4, sort_keys=True)

    @staticmethod
    def add_item(item: Item):
        db = Database.get()
        db.items[item.item_name] = item

        Database.write(db)

    @staticmethod
    def remove_item(item_name: str):
        db = Database.get()
        db.items.pop(item_name)

        Database.write(db)

    @staticmethod
    def add_profile(profile: Profile):
        db = Database.get()
        db.profiles[profile.profile_name] = profile

        Database.write(db)

    @staticmethod
    def remove_profile(profile_name: str):
        db = Database.get()
        db.profiles.pop(profile_name)

        Database.write(db)

    @staticmethod
    def set_owned(item_name: str):
        db = Database.get()
        db.profiles[Config.get().profile].owned_items.append(item_name)

        Database.write(db)

    @staticmethod
    def set_unowned(item_name: str):
        db = Database.get()
        if item_name in db.profiles[Config.get().profile].owned_items:
            db.profiles[Config.get().profile].owned_items.remove(item_name)

        Database.write(db)
