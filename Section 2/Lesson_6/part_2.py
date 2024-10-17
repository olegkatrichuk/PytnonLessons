# task1


# num = int(input('Enter a number : '))
#
#
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# res = is_even(num)
# print(res)

# task 2

# new_str = input('Enter a string : ')
#
#
# def count_vowels(s):
#     temp = 'аоуеяюиэыё'
#     counter = 0
#     for i in s:
#         if i in temp:
#             counter += 1
#
#     return counter
#
#
# res = count_vowels(new_str)
# print(f'Count of vowels : {res}')

# task 3

# new_str = input('Enter a string : ')
#
# lst = new_str.split()
#
# def count_vowels(s):
#     return max(s)
#
# max = count_vowels(lst)
# print(f'Max number is {max}')

# task 4

# new_str = input('Enter a string : ')
#
#
# def reverse_string(s):
#     return s[::-1]
#
#
# reversed_str = reverse_string(new_str)
# print(reversed_str)

# task 5

# a = input('Enter a number a : ')
# b = input('Enter a number b : ')
# c = input('Enter a number c : ')

# def check_num(a, b, c):
#     def is_number_or_not(temp):
#         try:
#             float(temp)
#             return True
#         except ValueError:
#             return False
#
#     return is_number_or_not(a) and is_number_or_not(b) and is_number_or_not(c)
#
#
# print(check_num(a, b, c))

# task 6

# print('To exit the program, press : z ')
#
# while True:
#     number1 = input('Enter a number1 : ').lower()
#     if number1 == 'z':
#         break
#     number2 = input('Enter a number2 : ').lower()
#     if number2 == 'z':
#         break
#     operation = input('Enter a operation  ( +, -, /, * ) : ').lower()
#     if operation == 'z':
#         break
#     else:
#         if operation == '+':
#             print(float(number1) + float(number2))
#         elif operation == '-':
#             print(float(number1) - float(number2))
#         elif operation == '/':
#             print(float(number1) / float(number2))
#         elif operation == '*':
#             print(float(number1) * float(number2))
#         else:
#             print('Invalid operation')

# task 7

# btc_balance = float(input('Enter a balance BTC : '))
# eth_balance = float(input('Enter a balance ETH : '))
#
# name_crypto = input('Enter a BTC or ETH : ')
# new_amount = float(input('Enter amount : '))
#
#
# def can_afford_transaction(currency, amount):
#     global btc_balance, eth_balance
#
#     if currency == 'BTC':
#         return btc_balance + amount > 0
#
#     elif currency == 'ETH':
#         return eth_balance + amount > 0
#
#     else:
#         return False
#
#
# def update_balance(currency, amount):
#     global btc_balance, eth_balance
#
#     if can_afford_transaction(currency, amount) > 0:
#
#         if currency == 'BTC':
#             btc_balance += amount
#             print(f'BTC : {btc_balance}')
#         elif currency == 'ETH':
#             eth_balance += amount
#             print(f'ETH : {eth_balance}')
#     else:
#         print('Not enought money')
#
#
# update_balance(name_crypto, new_amount)
