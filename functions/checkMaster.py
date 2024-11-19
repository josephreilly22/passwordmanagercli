import json
from functions.hashPassword import *
from functions.aesEncrypt import *
from functions.aesDecrypt import *

import getpass

from colorama import Fore, Back, Style

def checkMaster(master=None):
    with open('data/check.json', 'r') as file:
        file_data = json.load(file)

    if 'ct' not in file_data:
        print('\n-----Create Master Password-----\n')
        while True: 
            print(Fore.LIGHTRED_EX)
            print('Remember your password! This can not be reset and passwords will be lost forever!')
            print(Style.RESET_ALL)
            master_password = getpass.getpass('Set Master Password: ')
            master_password_again = getpass.getpass('Again: ')
            if master_password == master_password_again:
                hashed = hashPassword(master_password)
                store_value = aesEncrypt(hashed['bytes'], hashed['string'])
                with open('data/check.json', 'w') as file:
                    print(1)
                    json.dump(store_value, file)
                print(Fore.GREEN)
                print('Master Password Set')
                break
            else: 
                print('Passwords did not match')
    else:
        try:
            with open('data/check.json', 'r') as file:
                file_data = json.load(file)
            hashed = hashPassword(master)
            decrypted = aesDecrypt(hashed['bytes'], file_data['ct'], file_data['iv'])
            if bytes(hashed['string'], 'utf-8') == decrypted:
                return hashed['bytes']
            else: 
                return False
        except:
            return False

