import aredis
import re
from . import settings


keys_pattern = re.compile(r'[A-Z,_]+')
settings_dict = vars(settings)
settings_keys = [
    key for key in settings_dict.keys()
    if keys_pattern.match(key)
]
app_settings_dict = {
    key: value for key, value in settings_dict.items()
    if key in settings_keys 
}


class AppConfiguration(object):
    def __init__(self, app):
        self.app = app

    def __getattr__(self, name):
        if name in app_settings_dict:
            return app_settings_dict.get(name)
        raise AttributeError("Attribute %s Not Found" % name)
