import json


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Configuration(metaclass=SingletonMeta):

    def __init__(self):
        self.config = self.load()

    def load(self):
        with open("config/config.json") as f:
            config = json.load(f)
        return config

    def get(self, key_name):
        return self.config.get(key_name)
