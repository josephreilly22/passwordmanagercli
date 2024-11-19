from functions.aesDecrypt import *
import json


def getPassword(key, value):
    with open('data/passwords.json', 'r') as file:
        file_data = json.load(file)
    
    if value in file_data:
        password = aesDecrypt(key, file_data[value]['ct'], file_data[value]['iv'])
        return password
    else:
        return False
