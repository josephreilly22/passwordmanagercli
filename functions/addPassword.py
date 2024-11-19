import json
from functions.aesEncrypt import *


def addPassword(value, password, key):
    try:
        with open('data/passwords.json', 'r') as file:
            file_data = json.load(file)
        encrypted_password = aesEncrypt(key, password)
        file_data[value] = encrypted_password
        with open('data/passwords.json', 'w+') as file:
            json.dump(file_data, file)
        return True
    except:
        return False
