# task 1

num = int(input('Enter a number : '))

def output_btc(value):
    for i in range(value):
        print("BTC", end=' ')

output_btc(num)

# task 2

num = int(input('Enter a number : '))

def factorial(value):
    fact = 1
    for i in range(1, value + 1):
        fact *= i

    print(f'Factorial = {fact}')

factorial(num)

# task 3

price = float(input('Enter your first price : '))
price_new = float(input('Enter your new price : '))


def price_change(initial_price, final_price):
    if initial_price < final_price:
        result = final_price - initial_price
        print(f'The price of BTC rose by {(result / initial_price) * 100:10.2f} %')
    if initial_price > final_price:
        result = initial_price - final_price
        print(f'The price of BTC fell by {(result / initial_price) * 100:10.2f} %')


price_change(price, price_new)

# task 4

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))


def calc(value1, value2):
    print(f'{value1} + {value2} = {value1 + value2}')
    print(f'{value1} - {value2} = {value1 - value2}')
    print(f'{value1} * {value2} = {value1 * value2}')
    if value2 != 0:
        print(f'{value1} / {value2} = {value1 / value2}')
    print(f'{value1} ** {value2} = {value1 ** value2}')


calc(num1, num2)
