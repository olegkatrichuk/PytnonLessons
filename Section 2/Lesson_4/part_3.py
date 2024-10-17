# task 1
import re

# text = input('Enter a json : ')
# value_input = input('Enter a value : ')
#
# lst = text.split(',')
# dict1 = {}
#
# for item in lst:
#     key, value = item.split(':')
#     dict1[key] = value
#
# print(dict1)
#
# for key, value in list(dict1.items()):
#     if value == value_input:
#         del dict1[key]
#
# print(dict1)

# task 2

# text = input('Enter a string : ')
#
# char = list(text)
#
# dict1 = {}
#
# for i in char:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#
# print(dict1)

# task 3

# text = input('Enter a json : ')
# factor = int(input('Enter a factor : '))
#
# lst = text.split(',')
#
# dict1 = {}
#
# for i in lst:
#     key, value = i.split(':')
#     dict1[key] = value
#
# print(dict1)
#
# for key, value in dict1.items():
#     if value.isdigit():
#         dict1[key] = int(value) * factor
#
# print(dict1)

# task 4

# text = input('Enter a json : ')
# value_input = input('Enter a value : ')
#
# lst = text.split(',')
# dict1 = {}
# new_lst = []
#
# for i in lst:
#     key, value = i.split(':')
#     dict1[key] = value
#
# for key, value in dict1.items():
#     if value == value_input:
#         new_lst.append(key)
#
# print(new_lst)

# task 5

# text = input('Enter a text : ')
#
# lst = re.split('[ ,.!?-]', text)
# dict1 = {}
#
# for i in lst:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#
# print(dict1)

# task 6

# str1 = input('Enter the first list of elements separated by commas : ')
# str2 = input('Enter a second list of items of the same length, separated by commas : ')
#
# lst1 = str1.split(',')
# lst2 = str2.split(',')
#
# dict1 = dict(zip(lst1, lst2))
#
# print(dict1)
#
# dict2 = {}
# for i in range(len(lst1)):
#     for j in range(len(lst2)):
#         if i == j:
#             dict2[lst1[i]] = lst2[j]
#
# print(dict2)
