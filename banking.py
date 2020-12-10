import sqlite3
import account
from cards import create_card
import menu_messages

try:
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    # cursor.execute("DROP TABLE card")
    cursor.execute(
        """CREATE TABLE card (
           id INTEGER NOT NULL PRIMARY KEY,
           number TEXT,
           pin TEXT,
           balance INTEGER DEFAULT 0
        );"""
    )
    # connection.commit()
    connection.close()
except Exception as e:
    # print("Table exists")
    pass

while True:
    menu_messages.main_menu()
    choice = int(input())
    if choice == 1:
        create_card()
        continue
    elif choice == 2:
        account.login()
    elif choice == 0:
        menu_messages.bye()
        exit()


# def luhn_check(number):
#     _sum = 0
#     for x in range(len(number) - 1):
#         num = int(number[x])
#         temp = num
#         if x % 2 == 0:
#             temp = num * 2
#         if temp > 9:
#             temp -= 9
#         _sum += temp
#     if (10 - _sum % 10) % 10 == int(number[len(number) - 1]):
#         return True
#     else:
#         return False
#
#
# print(luhn_check("4000001369130869"))
