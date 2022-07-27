import pathlib
from configparser import ConfigParser

class Config():
    def __init__(self):
        cfg = ConfigParser()
        cfg.read(str(pathlib.Path().parent.absolute()) + '/config/app_config.ini')
        self.URL_CHUCK_NORRIS = cfg.get('dev', 'URL_CHUCK_NORRIS')
        self.URL_DAD_JOKES = cfg.get('dev', 'URL_DAD_JOKES')