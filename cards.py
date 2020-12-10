import random
import sqlite3
import menu_messages


def check_number(number):
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    cursor.execute(f"""SELECT COUNT(*)
                   FROM card"
                   "WHERE number = {number}""")
    card_exist = cursor.fetchone()[0] > 0
    connection.close()
    return card_exist


def check_credentials(number, pin):
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    cursor.execute(f"""SELECT pin, balance
                   FROM card
                   WHERE number = '{number}'""")
    cred = cursor.fetchone()
    if cred is None or cred[0] != pin:
        connection.close()
        return -1
    connection.close()
    return cred[1]


def luhn():
    temp = '400000'
    _sum = 8
    for x in range(7, 16, 1):
        n = random.randint(0, 9)
        temp += str(n)
        if x % 2 != 0:
            n *= 2
        if n > 9:
            n -= 9
        _sum += n
    n = (10 - _sum % 10) % 10
    temp += str(n)
    return temp


def luhn_check(number):
    _sum = 0
    for x in range(len(number) - 1):
        num = int(number[x])
        temp = num
        if x % 2 == 0:
            temp = num * 2
        if temp > 9:
            temp -= 9
        _sum += temp
    if (10 - _sum % 10) % 10 == int(number[len(number) - 1]):
        return True
    else:
        return False


def create_card():
    cn = luhn()
    while check_number(cn):
        cn = luhn()
    pin = str(random.randint(1000, 9999))
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO card (number, pin)
                      VALUES (:number, :pin)""", {'number': cn, 'pin': pin})
    connection.commit()
    connection.close()
    menu_messages.card_created(cn, pin)


def increase_balance(number, income):
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE card SET balance = balance + :income 
                      WHERE number = :number""", {'number': number, 'income': income})
    connection.commit()
    connection.close()


def decrease_balance(number, amount):
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE card SET balance = balance - :amount 
                      WHERE number = :number""", {'number': number, 'amount': amount})
    connection.commit()
    connection.close()


def delete_account(number):
    connection = sqlite3.connect("card.s3db")
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM card  
                      WHERE number = :number""", {'number': number})
    connection.commit()
    connection.close()
