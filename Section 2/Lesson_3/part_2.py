# task 1
import random

# random number generation
lst = []
i = 0
while i < 10:
    c = random.randint(1, 10)
    lst.append(c)
    i += 1
print(lst)

for i in lst:
    print(i, end=' ')
    if i == 5:
        print('The number 5 is found ')
        break


# task 2


for i in range(1, 11):
    if i % 3 == 0:
        continue
    else:
        print(i)
    if i == 7:
        break


# task 3

for i in range(1, 21):
    temp1 = i
    temp2 = i + 1

    if i % 4 == 0 or i % 5 == 0:
        continue
    else:
        print(i)
    if temp1 + temp2 > 30:
        break


# task 4

i = 1
while i < 21:
    if i % 3 == 0:
        i += 1
        continue
    else:
        print(i)
    i += 1
    if i == 15:
        break


# task 5

while True:
    num = int(input('Enter a number : '))
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(f'{num} - the number is prime')
    else:
        print(f'{num} - Compound number')

    if num == 0:
        break

# task 6

while True:
    current_balance = float(input('Enter a current balance : '))
    transfer_amount = float(input('Enter a transfer number : '))
    if transfer_amount <= current_balance:
        res = current_balance - transfer_amount
        print(f'New balance is - {res:10.2f}')
        break
    else:
        print('Not enough funds')
        continue

