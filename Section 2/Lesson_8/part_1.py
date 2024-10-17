# task 1
import random

# def load_wallets(filename):
#     with open(filename, 'r') as file:
#         content = file.readlines()
#         for wallet in content:
#             print(wallet.strip())
#
#
# def mix_wallets(filename):
#     with open(filename, 'r') as file:
#         content = file.readlines()
#         lst = random.sample(content, len(content))
#         for wallet in lst:
#             print(wallet.strip())
#
#
# load_wallets('wallets.txt')
# print('-----------------------------------------')
# mix_wallets('wallets.txt')

# task 2

# def load_wallets(filename):
#     with open(filename, 'r') as file:
#         content = file.readlines()
#         for wallet in content:
#             print(wallet.strip())
#     return content
#
#
# def generate_random_wallet_value(wallets):
#     new_wallet = random.choice(wallets)
#     new_value = random.random()
#     return new_wallet, new_value
#
#
# def save_wallet_to_file(wallet, value, filename):
#     with open(filename, 'w+') as new_file:
#         new_file.write(f"{wallet}: {value}\n")
#
#
# wallets = load_wallets('wallets.txt')
# wallet, value = generate_random_wallet_value(wallets)
# save_wallet_to_file(wallet, value, 'wallet.txt')
#
# print(f"Random wallet: {wallet}Random number: {value}")

# task 3

# def load_wallets(filename):
#     with open(filename, 'r') as file:
#         content = file.readlines()
#         for wallet in content:
#             print(wallet.strip())
#     return content
#
#
# def all_wallets(wallets):
#     random.sample(wallets, len(wallets))
#     large_wallets = []
#     small_wallets = []
#
#     for wallet in wallets:
#         num_float = round(random.uniform(0.001, 0.5), 5)
#         if num_float > 0.2:
#             large_wallets.append(f'{wallet}: {num_float}')
#             with open('large.txt', 'w') as large_file:
#                 large_file.write("\n".join(large_wallets) + "\n")
#         else:
#             small_wallets.append(f'{wallet}: {num_float}')
#             with open('small.txt', 'w') as small_file:
#                 small_file.write("\n".join(small_wallets) + "\n")
#
#
# my_wallets = load_wallets('wallets.txt')
#
# all_wallets(my_wallets)

# task 4

# psw = input('Enter a password : ')
#
#
# def check_password(password):
#     temp = '!@#$%^&*()'
#     char_upper = False
#     char_lower = False
#     char_digit = False
#     char_special = False
#
#     if len(password) < 8 or len(password) > 16:
#         return False
#
#     for char in password:
#         if char.isupper():
#             char_upper = True
#         elif char.islower():
#             char_lower = True
#         elif char.isdigit():
#             char_digit = True
#         elif char in temp:
#             char_special = True
#
#     if not char_upper:
#         return False
#     if not char_digit:
#         return False
#     if not char_lower:
#         return False
#     if not char_special:
#         return False
#
#     return True
#
#
# print(check_password(psw))
