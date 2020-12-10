import cards
import menu_messages


def login():
    menu_messages.card_prompt()
    num = input()
    menu_messages.pin_prompt()
    pin = input()
    balance = cards.check_credentials(num, pin)
    if balance >= 0:
        menu_messages.access_provided()
        acc = Account(num, balance)
        acc.account_menu()
    else:
        menu_messages.access_denied()


class Account:

    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def account_menu(self):
        while True:
            menu_messages.account_menu()
            choice = input()
            if choice == '1':
                print(f'\nBalance: {self.balance}\n')
            elif choice == '2':
                self.add_income()
            elif choice == '3':
                self.do_transfer()
            elif choice == '4':
                self.close_account()
                menu_messages.account_deleted()
                return
            elif choice == '5':
                menu_messages.logged_out()
                return
            elif choice == '0':
                exit()

    def balance(self):
        print(f'Balance: {self.balance}')
        # print("Balance: ")

    def add_income(self):
        menu_messages.income_prompt()
        income = int(input())
        self.balance += income
        cards.increase_balance(self.number, income)
        menu_messages.income_added()

    def do_transfer(self):
        while True:
            menu_messages.transfer_prompt()
            transfer_to_number = input()
            if transfer_to_number == self.number:
                menu_messages.same_account()
            elif not cards.luhn_check(transfer_to_number):
                menu_messages.wrong_number()
            elif not cards.check_number(transfer_to_number):
                menu_messages.no_such_card()
            else:
                break
        menu_messages.transfer_amount()
        amount = int(input())
        if amount > self.balance:
            menu_messages.not_enough_money()
        else:
            cards.increase_balance(transfer_to_number, amount)
            cards.decrease_balance(self.number, amount)
            self.balance -= amount
            menu_messages.tranfer_completed()

    def close_account(self):
        cards.delete_account(self.number)
