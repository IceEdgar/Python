#Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет
# все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
import random
import time

_SIZE_BOARD: int = 8  # размер доски
# queens = [(1, 1), (2, 3), (3, 5), (3, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def check_queens(queens):
    for i in range(len(queens)):
        row_prev, col_prev = queens[i]
        for j in range(i + 1, len(queens)):
            row_next, col_next = queens[j]
            if (
                    row_prev == row_next or
                    col_prev == col_next or
                    abs(row_prev - row_next) == abs(col_prev - col_next)
            ):
                return False
    return True


def generate_boards():
    count = 0
    board_list = []
    while count < 4:
        temp_pack = []
        for i in range(_SIZE_BOARD):
            temp_pack.append((i + 1, random.randint(1, _SIZE_BOARD)))

        if check_queens(temp_pack):
            board_list.append(temp_pack)
            count += 1
    return board_list


# print(check_queens(queens))
if __name__ == '__main__':
    print(generate_boards())
    print(time.process_time())
# from itertools import combinations
#
# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True



# import random
# from itertools import combinations
#
# def generate_board():
#     # Генерируем случайную доску
#     board = []
#
#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board
#
# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True
#
# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list