# task 1

num = int(input('Enter a number : '))

if num > 0:
    print('Positive number.')
elif num < 0:
    print('Negative number.')
else:
    print('Zero.')

# task 2

num = int(input('Enter a number from 1 to 100 :  '))

if 90 <= num <= 100:
    print('A')
elif 80 <= num <= 89:
    print('B')
elif 70 <= num <= 79:
    print('C')
elif 60 <= num <= 69:
    print('D')
else:
    print('F')

# task 3

current_value = float(input('Enter current value : '))
desired_value = float(input('Enter desired value : '))

if current_value < desired_value:
    print(f'You can buy cryptocurrency at the current price {current_value}')
else:
    print('You can not buy cryptocurrency at the current price ')

# task 4

price1 = float(input('Cryptocurrency purchase price : '))
price2 = float(input('Cryptocurrency selling price : '))

if price1 > price2:
    print(f'You lost money -{price1 - price2:10.2f} usdt.')
elif price2 > price1:
    print(f'You made : {price2 - price1:10.2f} usdt.')
else:
    print("You worked at zero ")

# task 5

max_price = float(input('Enter a maximum price : '))
min_price = float(input('Enter a minimum price : '))

temp = (max_price - min_price) * 10 / 100
print(temp)
if temp >= 10:
    print('High')
elif 1 < temp < 10:
    print('Average')
elif temp <= 1:
    print('Low')

# task 6

price1 = float(input('Cryptocurrency purchase price : '))
price2 = float(input('Cryptocurrency selling price : '))

if price1 > price2:
    print('Cryptocurrency price is higher than the current one.')
elif price1 <price2:
    print('Cryptocurrency price is lower than the current one.')
else:
    print('Cryptocurrency price is equal to the current one.')

# task 7

price = float(input('Cryptocurrency current price : '))
max_price = float(input('Maximum price in 2023 : '))

if price > max_price:
    res = price - max_price
    percent = res * 100 / max_price
    print(f'The price went up a {int(percent)} percent ')
elif price < max_price:
    res = max_price - price
    percent = res * 100 / price
    print(f'The price dropped by a {int(percent)} percent ')
else:
    print('The price has not changed')

# task 8

price_1 = float(input('Enter the current price of the first cryptocurrency : '))
price_2 = float(input('Enter the current price of the second cryptocurrency : '))

if price_1 > price_2:
    print(f'The first cryptocurrency is more expensive than the second by {price_1 - price_2:10.2f} usdt')
elif price_2 > price_1:
    print(f'The second cryptocurrency is more expensive than the first by {price_2 - price_1:10.2f} usdt')
else:
    print('The value of cryptocurrencies is the same.')

# task 9

price1 = float(input('Enter the current value of the cryptocurrency : '))
price_one_day = float(input('Enter the value of cryptocurrency in a day : '))

percent = price1 * 1 / 100
temp1 = price1 + percent
temp2 = price1 - percent

if round(temp1) == price_one_day or round(temp2) == price_one_day:
    print("Stable trend ")
elif price_one_day > price1:
    print('Growing trend ')
elif price1 > price_one_day:
    print('Falling trend ')
