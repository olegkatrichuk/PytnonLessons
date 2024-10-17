# task 1
import random
from pprint import pprint

# num = int(input('Enter a number : '))
#
# i = 2
#
# while i <= num:
#     j = 2
#     while j * j <= i:
#         if i % j == 0:
#             break
#         j += 1
#     if j * j > i:
#         print(i,end=' ')
#     i += 1

# task 2

# random number generation
# lst = []
# i = 0
# while i < 20:
#     c = random.randint(1, 20)
#     lst.append(c)
#     i += 1
# print(lst)
#
# counter = 0
# i = 0
# while i < len(lst):
#     if lst[i] > 10:
#         counter += 1
#         print(lst[i], end=' ')
#     i += 1
#
# print('\n'+ f'Number of elements - {counter}')

# task 3

# str1 = input('Enter a string : ').lower().strip()
# str2 = input('Enter another string : ').lower().strip()
#
# anagram = True
#
# dict1 = {}
# dict2 = {}
#
# if len(str1) != len(str2):
#     anagram = False
# else:
#     i = 0
#     while i < len(str1):
#         dict1[str1[i]] = dict1.get(str1[i], 0) + 1
#         i += 1
#
#     j = 0
#     while j < len(str2):
#         dict2[str2[j]] = dict2.get(str2[j], 0) + 1
#         j += 1
#
#     if dict1 == dict2:
#         anagram = True
#
# print(anagram)

# task 4

# num = int(input('Enter a number : '))
#
# sum1 = 0
#
# for i in range(1, num):
#     if num % i == 0:
#         sum1 += i
#
# if sum1 == num:
#     print(True)
# else:
#     print(False)

# task 5

# str1 = input('Enter a number : ')
#
# lst = str1.split()
#
# if len(lst) < 2:
#     print('Please enter a valid input')
#
# else:
#     i = 0
#     flag = True
#     while i < len(lst) - 1:
#         if lst[i] <= lst[i + 1]:
#             flag = True
#         else:
#             flag = False
#             break
#         i += 1
#
#     print(flag)

# task 6

# a = int(input('Enter a number : '))
# b = int(input('Enter a number : '))
#
# str1 = ''
#
# if a < b:
#     while a < b + 1:
#         str1 += str(a)
#         a += 1
# else:
#     while b < a + 1:
#         str1 += str(b)
#         b += 1
#
# print(str1)