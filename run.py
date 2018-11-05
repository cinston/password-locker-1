#!/usr/bin/env python3.6

from user import User
from credentials import Credentials
import random


def register_user(f_name, l_name, u_name, password):
    """
      Function that creates a new Password Locker user.
    """
    new_user = User(f_name, l_name, u_name, password)
    new_user.save_user()


def login_user():
    """
      Function that logs user to Password Locker.
    """
    username = input("Enter your username \n")
    password = input("Enter your password \n")

    if User.user_exists(username):
        for user in User.user_list:
            if username == user.username and password == user.password:
                return True
            else:
                print("Invalid username or password! Please try again.")
                # login_user() 
    else:
        print("User does not exist")  
        anykey = input('press any key to continue...')
        return False


def create_credentials(account_name, username, password):
    """
        Method that credentials new credentials
    """
    save_credentials(Credentials(account_name, username, password))


def save_credentials(cred):
    """
        Method that stores existing credentials
    """
    Credentials.cred_list.append(cred)


def display_credentials():
    """
        Method that displays all credentials
    """
    return Credentials.cred_list


def generate_password(length):
    """
        Method that generates passwords.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    password = ''
    for c in range(length):
        password += random.choice(chars)
    return password


def main():
    """
      The main function that runs before the other functions
    """
    while True:
        print("\033c")
        selection = input(
            "Welcome to Password Locker. use \n \n \"login\" - login to your account \n \"register\" - create a Password Locker. \n  \"exit\" - Exit the application \n \n").lower()
        print("." * 14)

        if selection == 'register':
            print("\033c")
            f_name = input("Enter your first name \n")
            l_name = input("Enter your last name \n")
            u_name = input("Enter your username \n")
            password = input("Enter a password \n")
            register_user(f_name,l_name,u_name, password)
            print('\n')
            print("User successfully created! \n")
            anykey = input('press any key to continue...')
            continue
        elif selection == 'login':
            print("\033c")
            logged_in = login_user()

            while logged_in:
                print("\033c")
                print(f" Welcome. Use the words :\n new - create new credentials,\n save - store existing credentials,\n display - display all credentials,\n quit - return to home")

                selected_word = input().lower()

                if selected_word == 'new':
                    print("\033c")
                    account_name = input('Enter account name \n')
                    u_name = input('Enter username \n')
                    choice = input(
                        'Would you like to generate a password?(yes/no) \n').lower()
                    if choice == 'yes':
                        length = int(input('Enter password length \n'))
                        password = generate_password(length)
                    else:
                        password = input('Enter password \n')

                    create_credentials(account_name, u_name, password)
                elif selected_word == 'save':
                    print("\033c")
                    account_name = input('Enter account name \n')
                    u_name = input('Enter username \n')
                    password = input('Enter password \n')

                    create_credentials(account_name, u_name, password)
                    print("Successfully added! \n")
                    anykey = input('press any key to continue...')
                elif selected_word == 'display':
                    print("\033c")
                    logged_in = login_user()
                    if logged_in and Credentials.cred_list:
                        print("\033c")
                        print("The following is a list of all your accounts")
                        print("\n")

                        for account in display_credentials():
                            print("-"*10)
                            print(f"Account: {account.account_name}")
                            print(f"Login: {account.username}")
                            print(f"Password: {account.password}")
                            print('\n')
                    else:
                        print('\n')
                        print("You dont seem to have any contacts saved yet")
                        print('\n')

                    print('\n \n')
                    anykey = input('press any key to continue...')
                elif selected_word == 'quit':
                    print('Goodbye!')
                    break
                else:
                    print("Invalid Input")
        else:
            print("Thank you for using Password Locker. Goodbye.")
            break


if __name__ == '__main__':
    main()
