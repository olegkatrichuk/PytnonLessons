# task 1

# text = input('Enter a text : ')
#
# with open('user_input.txt','w') as file:
#     file.write(text)
#
# with open('user_input.txt','r') as file:
#     content = file.read()
#     print(content)

# task 2

# text1 = input('Enter a text1 : ')
# text2 = input('Enter a text2 : ')
# text3 = input('Enter a text2 : ')
#
# with open('multi_line.txt', 'w') as file:
#     file.write(text1 + '\n' + text2 + '\n' + text3)
#
# with open('multi_line.txt', 'r') as file:
#     content = file.readlines()
#     for line in content:
#         print(line.strip())

# task 3

# text = input('Enter a text : ')
#
# with open('example.txt', 'w') as file:
#     file.write(text)
#
# with open('example.txt', 'r+') as file:
#     content = file.read()
#     update = content.replace('old', 'new')
#     file.seek(0)
#     file.write(update)
