# task 1

degree_c = float(input('Enter degrees Celsius : '))

degree_f = degree_c * 9 / 5 + 32

print(f'Celsius degrees {degree_c} C. It will be fahrenheit {round(degree_f, 1)} F')

# task 2

price = float(input('Enter a price : '))
discount = int(input('Enter a discount : '))

temp = price * discount / 100
price_with_discount = price - temp

print(f'Cost of goods including shipping costs { price_with_discount: 10.2f} $ ')

# task 3

num = int(input('Enter a number : '))

if num % 2 == 0:
   print('Even number.')
else:
    print('Odd number.')

# task 4

length = int(input('Enter a length : '))
width = int(input('Enter a width : '))

s = length * width
p = 2 * (length + width)

if length == width:
   print(f'It is a square. Its area is : {s} and perimeter : {p}')
else:
    print(f'It is a rectangle. Its area is : {s} and perimeter : {p} ')

# task 5

column1 = int(input('Введите номер столбца для первой клетки : '))
str1 = int(input('Введите номер строки для первой клетки : '))
column2 = int(input('Введите номер столбца для второй клетки : '))
str2 = int(input('Введите номер строки для второй клетки : '))

res_column = 0
res_str = 0

if 1 <= column1 <= 8 and 1 <= str1 <= 8 and 1 <= column2 <= 8 and 1 <= str2 <= 8:
    if column1 > column2 or str1 > str2:
        res_column = column1 - column2
        res_str = str1 - str2
    else:
        res_column = column2 - column1
        res_str = str2 - str1

    if (res_column <= 1 and res_str <= 1) and not (res_column == 0 and res_str == 0):
        print("Ход допустим")
    else:
        print("Так король ходить не может")
else:
    print("Вы ввели некорректные координаты")
