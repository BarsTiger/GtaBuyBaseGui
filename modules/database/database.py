import json
from .model import DatabaseModel, default_database
from modules.config import Config
import os


class Database:
    @staticmethod
    def get():
        try:
            return DatabaseModel.from_dict(json.load(open(Config.get().database)))
        except:
            with open(Config.get().database, 'w') as f:
                json.dump(default_database, f, indent=4)
            return DatabaseModel.from_dict(default_database)
