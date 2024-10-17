# matrix = [
#     [2, 7, 6],
#     [9, 5, 1],
#     [4, 3, 8]
# ]
#
# len_matrix = len(matrix)
# len_rows = sum(matrix[0])
# len_rows1 = sum(matrix[1])
#
# magic_verif = True
#
# if len_rows != len_rows1:
#     magic_verif = False
#
# elif magic_verif:
#
#     for col in range(len_matrix):
#         column_sum = 0
#         for row in range(len_matrix):
#             column_sum += matrix[row][col]
#
#         if column_sum != len_rows:
#             magic_verif = False
#
#     diagonal_sum = 0
#     for i in range(len_matrix):
#         diagonal_sum += matrix[i][i]
#
#     if diagonal_sum != len_rows:
#         magic_verif = False
#
#     diagonal_sum = 0
#     for i in range(len_matrix):
#         diagonal_sum += matrix[i][len_matrix - 1 - i]
#
#     if diagonal_sum != len_rows:
#         magic_verif = False
#
# print(magic_verif)


# sum = 0
# for i in range(100):
#     num = int(input('Enter a number : '))
#     sum += num
#     if sum > 1000:
#         break
