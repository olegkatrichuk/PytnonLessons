# task 1 for
from itertools import count

from numpy import number

# num =  int(input('Enter a number : '))
#
# for i in range(1,num+1):
#     print(i,end=' ')

# task 2 for

# num = int(input('Enter a number : '))
#
# for i in range(1, num + 1):
#     if i % 2 != 0:
#         print(i, end=' ')

# task 3 for

# str1 = input('Enter a string : ')
#
# for i in str1:
#     print(i)

# task 4 for

# num = int(input('Enter a number : '))
#
# sum = 0
#
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         print(i)
#         sum += i
# print(sum)

# task 5 for

# for i in range(3, 10):
#     for j in range(1, 11):
#         if i % 2 != 0:
#             print(f'{i} * {j} = {i * j}')

# task 6 for

# str1 = input('Enter a string : ')
#
# for i in range(1,20):
#     print(f'{i} -  {str1}')

# task 7 for

# num1 = int(input('Enter a number1 : '))
# num2 = int(input('Enter a number2 : '))
#
# for i in range(num1, num2 + 1):
#     print(i)

# task 1 while

# num = int(input('Enter a number : '))
#
# i = 1
#
# while num + 1 > i:
#     print(num)
#     num -= 1

# task 2 while

# temp = int(input('Enter a number : '))
#
# sum = 1
# if temp == 0:
#     sum = 0
# else:
#     sum *= temp
#     while True:
#         num = int(input('Enter a number : '))
#         if num == 0:
#             print(f'You are entered {num}')
#             break
#         else:
#             sum *= num
# print(f'Summa = {sum}')

# task 3 while

# password ='1234'
#
# while True:
#     temp = input('Enter your password : ')
#     if temp==password:
#         print('Yes')
#         break

# task 4 while

# num = int(input('Enter a number : '))
#
# count = 0
#
# while num > 0:
#     count += 1
#     num //= 10
#
# print(count)

# task 5 while

# num = int(input('Enter a number : '))
#
# i = 1
#
# while i < num + 1:
#     print(i * 2)
#     i += 1

# task 1 list

# lst = [1,2,4,5,67,7]
# for i in  lst:
#     print(i,end=' ')

# task 2 list

# lst = [1, 2, 4, 5, 67, 7]
#
# sum = 0
#
# for i in lst:
#     sum += int(i)
#
# print(sum)

# task 3 list

# lst = [1, 2, 4, 5, 67, 7]
# lst1 = []
# for i in lst:
#     lst1.append(int(i) * 3)
# print(lst1)

# task 4 list

# lst = []
#
# for i in range(1, 6):
#     lst.append(i)
# print(lst)

# task 5 list

# lst = [1, 2, 4, 5, 67, 7]
#
# temp = lst.sort()
# print(temp)

# task 1 dict

# dict1 = {'Hana': 23, 'Milana': 34, 'Nina': 45}
#
# for key, value in dict1.items():
#     print(f'{key}:{value}')

# task 2 dict

# str1 = 'a:1,c:2,g:6,n:8'
#
# lst = str1.split(',')
# print(lst)
# dict1 = {}
#
# for i in lst:
#     key, value = i.split(':')
#     dict1[key] = value
#
# print(dict1)

# task 3 dict

# str1 = input('Enter a string : ')
# key = input('Enter a key : ')
#
# lst = str1.split(',')
#
# dict1 = {}
#
# for i in lst:
#     key, value = i.split(':')
#     dict1[key] = value
#
# if key in dict1:
#     print('Yes')
# else:
#     print('No')

# task 4 dict

# str1 = input('Enter a string : ')
#
# lst = str1.split(',')
# dict1 = {}
#
# for i in lst:
#     key, value = i.split(':')
#     dict1[key] = value
# print(len(dict1))
# count = 0
# for i in dict1:
#     if dict1[i].isalnum():
#         count += 1
# print(count)

# tas 5 dict

# str1 = input('Enter a string : ')
#
# lst = str1.split(',')
# dict1 = {}
#
# for i in lst:
#     key, value = i.split(':')
#     dict1[key] = value
# print(dict1)
# for key, value in dict1.items():
#     dict1[key] = 0
# print(dict1)
