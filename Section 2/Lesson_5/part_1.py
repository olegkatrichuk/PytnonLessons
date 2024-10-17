# task 1
from numpy.ma.core import count

# transaction = input('Enter a transaction number : ')
#
# lst = transaction.split()
#
# count = 0
#
# for i in lst:
#     if 1000 <= int(i) <= 5000 and int(i) % 2 != 0:
#         print(i)
#         count += 1
#
# print(f'Number of transactions {count}')

# task 2

# str1 = input('Enter a transaction number : ')
#
# lst = str1.split()
#
# count_neg = 0
# count_pos = 0
#
# for i in lst:
#     if int(i) > 0:
#         count_pos += 1
#     elif int(i) < 0:
#         count_neg += 1
#
# print(f'Positive number : {count_pos}')
# print(f'Negative number : {count_neg}')

# task 3

# letter = input('Enter a letter : ').lower()
#
# lst = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew","egg"]
#
# count = 0
# for i in lst:
#     if letter in i:
#         print(i)
#         count += 1
# print(f'Words with letter {letter} = {count}')

# task 4

# letter = input('Enter a letter : ')
#
# lst = ["apple", "banana", "Cherry", "date", "Elderberry", "fig", "GrapE", "honeydew","ferre"]
#
# count = 0
#
# for i in lst:
#     if i.endswith(letter):
#         count += 1
#
# print(f'Words with letter {letter} = {count}')