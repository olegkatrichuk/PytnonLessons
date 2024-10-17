# task 1


# text = input('Enter a text : ')
# substring = input('Enter a substring : ')
# new_substring = input('Enter a new substring : ')
#
# if substring.istitle():
#     text = text.replace(substring, new_substring.capitalize())
#
# new_str = substring.lower()
# text = text.replace(new_str, new_substring.lower())
#
# print(text)

# task 2

# numbers = input('Enter numbers separated by a space : ')
#
# lst = numbers.split()
# print(lst)
# print('Max number is ', max(lst))
# print('Min number is ', min(lst))
#
# max_num = int(lst[0])
# min_num = int(lst[0])
# for i in lst:
#     if int(i) < min_num:
#         min_num = int(i)
#     if int(i) > max_num:
#         max_num = int(i)
#
# print(f'Max number is {max_num}')
# print(f'Min number is {min_num}')

# task 3

# text = input('Enter a string : ')
#
# words = text.split(' ')
# print(words)
#
# new_text = ''.join(words[::-1])
# print(new_text)
#
# new_text1 = ''.join(reversed(words))
# print(new_text1)

# task 4

# numbers = input('Enter numbers separated by a space : ')
#
# lst = numbers.split(' ')
# print(lst)
#
# new_lst = []
# for i in lst:
#     if i in new_lst:
#         continue
#     else:
#         new_lst.append(i)
#
# print(sorted(new_lst))

# task 5

text = input('Enter a string : ')

char = list(text)

count_all_letter = 0
count = 0

for i in char:
    if i.isalpha():
        count_all_letter += 1
    if i == 'о' or i == 'а' or i == 'е' or i == 'и' or i == 'у' or i == 'я' or i == 'ы' or i == 'э' or i == 'ю' or i == 'ё':
        count += 1
print(f'Number of all letters - {count_all_letter}')
print(f'Number of vowel letters - {count}')
print(f'Number of consonant letters - {count_all_letter - count}')

# task 6

# text = input('Enter a string : ')
# char = input('Enter a character : ')
#
# count = 0
#
# words = text.split()
# print(words)
# for word in words:
#     if word.startswith(char):
#         count +=1
#
# print(count)

# task 7

numbers = input('Enter numbers separated by a space : ')

lst = numbers.split()
print(lst)

max_element = int(lst[0])
min_element = int(lst[0])
position_max = 0
position_min = 0

for i in range(len(lst)):
    if int(lst[i]) < min_element:
        min_element = int(lst[i])
        position_min = i
    if int(lst[i]) > max_element:
        max_element = int(lst[i])
        position_max = i

temp = lst[position_max]
lst[position_max] = lst[position_min]
lst[position_min] = temp

print(lst)
