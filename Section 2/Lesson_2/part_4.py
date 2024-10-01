# task 1

num = int(input('Enter a number : '))

if num % 3 == 0 and num % 5 == 0:
    print('Divisible by 3 and 5 ')
else:
    print('Not divisible by 3 and 5')


# task 2

time_now = int(input('Enter a time in hours : '))

if 6 <= time_now <= 11:
    print('Morning')
elif 12 <= time_now <= 17:
    print('Day')
elif 18 <= time_now <= 21:
    print('Evening')
elif 22 <= time_now <= 23 or 0 <= time_now <= 5:
    print('Night')
else:
    print('There is no time like the present ')


# task 3

crypto_name = input('Enter crypto name : ')

word = 'coin'

if crypto_name.endswith(word) and crypto_name.isalpha():
    print('Correct name ')
else:
    print('Incorrect name')

# task 4

balance_usdt = float(input('Enter your balance : '))
min_balance_usdt = float(input('Enter minimum purchase balance :'))

if balance_usdt >= min_balance_usdt:
    print('The balance is sufficient')
else:
    print('Balance is not enough')