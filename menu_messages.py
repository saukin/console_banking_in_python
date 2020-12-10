def main_menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')


def account_menu():
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')


def card_created(number, pin):
    print('\nYour card has been created\n'
          'Your card number:\n'
          f'{number}\n'
          'Your card PIN:\n'
          f'{pin}\n')


def card_prompt():
    print("\nEnter your card number:")


def pin_prompt():
    print("Enter your PIN:")


def access_denied():
    print("\nWrong card number or PIN!\n")


def access_provided():
    print("\nYou have successfully logged in!\n")


def income_prompt():
    print("\nEnter income:")


def income_added():
    print("Income added\n")


def transfer_prompt():
    print("Transfer \nEnter card number:")


def transfer_amount():
    print("Enter how much money you want to transfer:")


def same_account():
    print("You can't transfer money to the same account!")


def no_such_card():
    print("Such a card does not exist.\n")


def wrong_number():
    print("Probably you made a mistake in the card number. Please try again!\n")


def not_enough_money():
    print("Not enough money!\n")


def tranfer_completed():
    print("Success!\n")


def logged_out():
    print("\nYou have successfully logged out!\n")


def account_deleted():
    print("The account has been closed!")


def bye():
    print("\nBye!")
