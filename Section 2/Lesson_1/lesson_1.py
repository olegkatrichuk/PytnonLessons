# task 1

num = int(input('Введите целое число : '))
double = float(input('Введите  число с плавающей точкой : '))
name = input('Введите строку : ')

print(f'Целое число : {num}')
print(f'Число с плавающей точкой : {double}')
print(f'Строка : {name}')

# task 2

num1 = int(input('Введите первое целое число : '))
num2 = int(input('Введите второе целое число : '))

res = num1 * num2

print(f'Результат умножения чисе {num1} и {num2} будет - {res}')


double1 = float(input('Введите первое число с плавающей точкой : '))
double2 = float(input('Введите второе число  с плавающей точкой : '))

res = double1 + double2

print(f'Результат сложения чисел {double1} и {double2} будет - {res}')


double1 = float(input('Введите первое число с плавающей точкой : '))
double2 = float(input('Введите второе число  с плавающей точкой : '))
num_pow = int(input('Введите степень числа : '))

res = double1 + double2
power_num = res * num_pow
print(f'Результат сложения чисел {double1} и {double2} и возведения в степень {num_pow} будет - {power_num}')

# task 3

money = float(input("Введите сумму денег на которую хотите купить :"))
course = float(input('Введите текущую стоимость криптовалюты : '))

res = money / course

print(f'Вы можете купить криптовалюту - {res:10.6f} монет')

# task 4

money = float(input("Введите USDT на которую хотите купить : "))
course = float(input('Введите текущую цену криптовалюты : '))
percent = float(input('Введите процент комиссии : '))

res = money / course
temp = res * percent / 100
res = res - temp

print(f"Вы можете купить с учететом комисии - {res:10.6f} монет")

# task 5

sum_credit = float(input('Введите сумму кредита : '))
percent_of_year = float(input('Введите годовую процентную ставку  : '))
term_credit = int(input('Введите срок кредита в месяцах : '))

percent_of_month = percent_of_year / 12 / 100

val1 = percent_of_month * ((1 + percent_of_month) ** term_credit)
val2 = ((1 + percent_of_month) ** term_credit) - 1

res = sum_credit * (val1 / val2)

print(f"Ежемесячный платеж по кредиту будет составлять :{res:10.2f} рублей.")
