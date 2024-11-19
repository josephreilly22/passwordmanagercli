from functions.checkMaster import *
from functions.addPassword import *
from functions.getPassword import *

from colorama import Fore, Back, Style
from art import *
import getpass

import sys
import time
import random

def main():
    try:
        print(Fore.LIGHTRED_EX)
        tprint('Pass', font='block')
        tprint('Manage', font='block')
        checkMaster()
        while True:
            print(Fore.LIGHTCYAN_EX + '\nWhat would you like to do?')
            print('1. Add new password')
            print('2. Get password')
            print('3. Exit\n')
            input_choice = input('Choice: ')

            if input_choice == '1':
                name = input('Name of password: ')
                password = input('Password to store: ')
                print(Fore.LIGHTYELLOW_EX)
                master_password = getpass.getpass('Master Password: ')
                print(Fore.LIGHTCYAN_EX)
                check = checkMaster(master_password)
                if check:
                    if addPassword(name, password, check):
                        encrypt_array = list(range(26))
                        random.shuffle(encrypt_array)
                        encrypt_pass = ['*' for i in range(26)]
                        print('\nPassword: ', end=' ')
                        for i in encrypt_pass:
                            print(i, end='')
                        for i in encrypt_array:
                            sys.stdout.flush()
                            encrypt_pass[i] = 'X'
                            print('\rPassword: ', end=' ')
                            for i in encrypt_pass:
                                print(i, end='')
                            time.sleep(0.08)
                        print(Back.GREEN)
                        print(Fore.BLACK)
                        print('\nPASSWORD ENCRYPTED AND SAVED!\n')
                        print(Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTRED_EX)
                        print('An error occured\n')
                else:
                    print(Fore.LIGHTRED_EX)
                    print('Incorrect Master Password: Password not added\n')
            elif input_choice == '2':
                name = input('What is the name of the password you want? ')
                print(Fore.LIGHTYELLOW_EX)
                master_password = getpass.getpass('Master Password: ')
                check = checkMaster(master_password)
                if check:
                    password = getPassword(check, name)
                    if password:
                        print(Fore.GREEN)
                        reveal = input('Password Found! Would you like to reveal(y/): ')
                        if reveal.capitalize() == 'Y':
                            print(f'\nPassword: {password.decode('utf-8')}\n')
                        else:
                            print(Style.RESET_ALL)
                            print(Fore.LIGHTCYAN_EX)
                            print('Password Not Revealed\n')
                    else:
                        print(Fore.LIGHTRED_EX)
                        print(f'No password called: {name}\n')
                else:
                    print(Fore.LIGHTRED_EX)
                    print('Incorrect Master password\n')
            elif input_choice == '3':
                print(Fore.LIGHTCYAN_EX)
                tprint('BYE', font='rnd-large')
                print('\n')
                print(Style.RESET_ALL)
                break
            else:
                print(Back.LIGHTRED_EX)
                print('Not Valid Choice, try again\n')
    except:
        print(Fore.LIGHTRED_EX)
        tprint('ERROR')
        print(Style.RESET_ALL)



if __name__ == '__main__':
    main()
