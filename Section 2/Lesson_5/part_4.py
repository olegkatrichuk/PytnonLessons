# task 1

# str1 = input('Enter a string : ')
# number = input('Enter a number : ')
# new_number = input('Enter a new number : ')
#
# lst = str1.split()
# str2 = ''
#
# for i in lst:
#     if i.isdigit() and i == number and int(i) > 0 and int(i) % 2 == 0 and len(i) == 3:
#         str2 += ' ' + new_number
#     else:
#         str2 += ' ' + i
#
# print(str2.strip())

# task 2

# number = int(input('Enter a number : '))
#
# for i in range(1, number + 1):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i,end=' ')

# task 3

# str1 = input('Enter a numbers : ')
#
# lst = str1.split()
#
# counter = 0
#
# for i in lst:
#     if 5 < int(i) < 15:
#         counter += 1
#
# print(f'Number of elements - {counter}')

# task 4

# str1 = input('Enter a strings : ')
#
# lst = str1.split()
#
# lst_new = []
#
# for i in lst:
#     if i in lst_new:
#         continue
#     else:
#         lst_new.append(i)
#
# if lst == lst_new:
#     print(True)
# else:
#     print(False)

# task 5

# str1 = input('Enter a strings : ')
#
# lst = str1.split()
#
# for i in lst:
#     if i.isdigit() and int(i) % 2 == 0 and int(i) > 10:
#         print(i,end=' ')
