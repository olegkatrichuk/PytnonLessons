# task 1


# num = int(input('Enter a number : '))
#
# sum = 0
# if num > 0:
#     for i in range(1, num + 1):
#         sum += i
#     print(sum)
# elif num < 0:
#     for i in range(num, 2):
#         sum -= i
#     print(f'- {sum}')
# else:
#     print('You entered a zero')

# task 2

# lst = [1, 2, -3, 4, -5, 11, -43, 32, 'hello', [5, 5, -1]]
#
# sum = 0
# last_element = lst[-1]
#
# for i in range(len(lst)):
#     if type(lst[i]) == int and lst[i] > 0:
#         sum += lst[i]
#
# for j in range(len(last_element)):
#     if last_element[j] > 0:
#         sum += last_element[j]
#
# print(f'Sum of positive elements of the list - {sum}')

# task 3

# num = int(input('Enter a number : '))
#
# lst = []
#
# for i in range(1, num + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         lst.append(i)
#
# print(lst)

# task 4

# lst = [11, 42, 37, 48, 71, 654]
#
# sum1 = 0
# sum2 = 0
#
# for i in range(len(lst)):
#     if i % 2 == 0:
#         sum1 += lst[i]
#     else:
#         sum2 += lst[i]
#
# print(sum1,sum2)
# print(f'Div {sum1} / {sum2} = {sum1/sum2}')

# task 5

# list_1 = ['ETH', 'BTC', 'XRP', 'HMSTR']
# list_2 = ['DOGS', 'CATS', 'APT']
# list_3 = ['ETH', 'BTC', 'XRP', 'HMSTR']
# list_4 = ['HMSTR', 'DOGS', 'CATS', 'APT']
#
# if list_1[-1] != list_2[0]:
#     print('False')
# if list_3[-1] == list_4[0]:
#     print('True')

# task 6

# web_sites = ['http://www.example.com', 'https://www.example.org', 'www.example.net', 'http://another.site',
#              'https://www.AntonProfit.com']
#
# lst1 = []
#
# for i in web_sites:
#     if i.endswith('.com') and i.startswith('https://'):
#         lst1.append(i)
#
# print(lst1)

# task 7

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237,
#            412, 566, 826,
#            248, 866, 950, 626, 949, 687, 217]
#
# for number in numbers:
#     if number % 2 == 0:
#         print(number)
#     if number == 237:
#         print(number)
#         break

# task 8

# str = input('Enter a string : ')
# print(str)
# print(str[::-1])
# str1 = ''.join(reversed(str))
# print(str1)

# task 9

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# lst = []
#
# for i in b :
#     if i in a:
#         lst.append(i)
#
# print(lst)

# task 10

# lst = [15, 35, 43, -10, 77]
#
# percent = 10
# for i in range(len(lst)):
#     lst[i] *= 1 + percent/100
#
# print(lst)

# task 11

# num = int(input('Enter a number : '))
#
# sum =0
# str1=str(num)
# lst = list(str1)
# print(lst)
# for i in range(len(lst)):
#      print(lst[i])
#      sum += int(lst[i])
#
# print(sum)

# task 12

# str1 = "Профит академия сделает из меня мастера по Питонам."
#
# count = 0
#
# for i in str1:
#     i.lower()
#     if i == 'о' or i == 'а' or i == 'е' or i == 'и' or i == 'у' or i == 'я':
#         count += 1
#
# print(count)

# task 13

num = int(input('Enter a number : '))

lst = []
lst2 = []
for i in range(1, num + 1):
    lst.append(i)
print(lst)

for i in range(1, num + 1):
    lst2.append(i * i)
print(lst2)
dict1 = dict(zip(lst, lst2))
print(dict1)