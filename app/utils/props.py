import configparser
import os 

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../config/config.ini'))

class ReadConfig:
    @staticmethod
    def get_base_url():
        base_url = config.get(section='main config', option='base_url')
        return base_url

    @staticmethod
    def get_login():
        login = config.get('main config', 'login')
        return login
    
    @staticmethod
    def get_password():
        password = config.get('main config', 'password')
        return password


    
