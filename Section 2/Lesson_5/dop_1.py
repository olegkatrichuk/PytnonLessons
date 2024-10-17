# task 1
# from multiprocessing.managers import Value
from itertools import count

# students = {'Виктория': 85, 'Мария': 92, 'Сергей': 78, 'Дмитрий': 90}
#
# new_student = {}
#
# sorted_value = sorted(students.values())
# sorted_value = sorted_value[::-1]
# print(sorted_value)
#
# for value in sorted_value:
#     for key, val in students.items():
#         if val == value and key not in new_student:
#             new_student[key] = value
#
# print(new_student)

# task 2

# store1 = {'яблоко': 50, 'банан': 30, 'апельсин': 40}
# store2 = {'банан': 25, 'апельсин': 60, 'клубника': 20}
#
# store3 = {}
#
# for key, value in store1.items():
#     for key1, value1 in store2.items():
#         if key1 == key:
#             store3[key] = value1 + value
#         elif key not in store3 or key1 not in store3:
#             store3[key] = value
#             store3[key1] = value1
#
# print(store3)

# task 3

# test_results = {'Анна': 75, 'Максим': 85, 'Андрей': 60, 'София': 90}
#
# dict1 = {}
# print(test_results)
# for key, value in test_results.items():
#     if int(value) > 80:
#         dict1[key] = value
#
# print(dict1)

# task 4

# sentence = "hello world hello Python hi student I love Python"
#
# lst = sentence.split()
# dict1 = {}
#
# for i in lst:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#
# print(dict1)

# task 5

# city_codes = {'Москва': +7495, 'Санкт-Петербург': +7812, 'Киев': +38044}
#
# dict1 = {}
# print(city_codes)
#
# for key, value in city_codes.items():
#     dict1[value] = key
#
# print(dict1)

# task 1

# price = int(input('Enter a number : '))
#
# percent = price * 10 / 100
# new_price1 = price + percent
# new_price2 = price - percent
#
# while True:
#     new_price = int(input('Enter a number : '))
#
#     if new_price < new_price1 or new_price < new_price2:
#         break

# task 2

# number = int(input('Enter a number : '))
#
# sum = 0
#
# if number > 0:
#     while number > 0:
#         if number % 2 == 0:
#             sum += number
#         number -= 1
#     print(sum)
# elif number < 0:
#     while number < 0:
#         if number % 2 == 0:
#             sum -= number
#         number += 1
#     print(-sum)

# task 3

# num = int(input('Enter a number : '))
#
# sum = 0
#
# while num > 0:
#     sum += num % 10
#     num //= 10
#
# print(sum)

# task 4

# num = int(input('Enter a number : '))
#
# num1 = 0
#
# while num > 0:
#     temp = num % 10
#     num = num//10
#
#     num1 = num1 * 10 + temp
#
# print(num1)

# task 5

# str1 ='1234'
#
# while True:
#     password = input('Enter a password : ')
#     if password == str1:
#         break
#     else:
#        continue

# task 6

# lst = [-1,-5,-2,3,0,4,1]
# print(lst)
#
# for j in range(len(lst) - 1):
#     for i in range(len(lst) - 1):
#         if int(lst[i]) > int(lst[i + 1]):
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     print(lst)
# print(lst)

