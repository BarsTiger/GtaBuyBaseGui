from modules.config.model import ConfigModel
import json


class Config:
    @staticmethod
    def default():
        return {
            "database": "default.gtabase",
            "profile": None,
            "theme": "Dark gray"
        }

    @staticmethod
    def fix() -> None:
        try:
            with open("config.cfg", "w") as file:
                json.dump(Config.default(), file)
        except FileNotFoundError:
            Config.fix()

    @staticmethod
    def get() -> ConfigModel:
        try:
            with open("config.cfg", "r") as file:
                return ConfigModel.from_dict(json.load(file))
        except:
            Config.fix()
            return Config.get()

    @staticmethod
    def update(key: str, value: str | None) -> dict:
        with open("config.cfg", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("config.cfg", "w") as file:
            json.dump(settings, file)

        return settings
