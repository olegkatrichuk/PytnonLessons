# task 1

def is_number():
    while True:
        num = input('Enter a number : ')
        try:
            num_int = int(num)
            print(f'You entered a number {num_int}')
            return num_int
        except ValueError:
            print('Please enter a number.')


print(is_number())

# task 2

try:
    def write_file(a: int):
        with open('example.txt', 'a') as file:
            file.writelines(str(a) + ' ')

    numbers = input('Enter a numbers : ')

    lst = numbers.split()

    for num in lst:
        new_num = int(num)
        write_file(new_num)

except ValueError:
    print('Please enter a number.')
else:
    print('All successfully done!')

# task 3

try:

    file_name = input("Enter file name : ")
    new_file_name = input('Enter new file name: ')


    def load_file(filepath):
        with open(filepath, 'r') as file:
            content = file.readlines()
        return content


    def upper_file(lst, filepath):
        new_lst = []
        for i in lst:
            new_lst.append(i.upper())

        with open(filepath, 'w') as file:
            file.write(' '.join(new_lst))


    res = load_file(file_name)
    upper_file(res, new_file_name)

except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Error: You do not have permission to read the file')
else:
    print('All successfully done!')

# task 4

file_name_1 = input("Enter one file name : ")
file_name_2 = input('Enter two file name: ')
save_file = input('Enter your save file name : ')

try:
    def load_file(filepath):
        with open(filepath, 'r') as file:
            content = file.readlines()
        return content


    def save_files(one_file, two_file, three_file):
        one_file_1 = load_file(one_file)
        two_file_1 = load_file(two_file)
        two_files = one_file_1 + two_file_1

        with open(three_file, 'w') as file:
            file.write(' '.join(two_files))


    save_files(file_name_1, file_name_2, save_file)

except FileNotFoundError as error:
    print(f'File not found {error.filename}')
except PermissionError as error:
    print(f"Error: You do not have permission to the file {('read' if error.filename in [file_name_1, file_name_2] else 'write' )} file '{error.filename}'.")
else:
    print('All successfully done!')