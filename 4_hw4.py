#Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов).
#Двумерный массив заполнен числами от 1 до 9.
#Функция должна вернуть False, если в массиве все числа от 1 до 9 встречаются ровно один раз.
#В противном случае True.
#Примеры вызовов.
#any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]]) ➞ False
#any_duplicates([[8, 9, 2], [5, 6, 1], [3, 7, 4]]) ➞ False
#any_duplicates([[1, 1, 3], [6, 5, 4], [8, 7, 9]]) ➞ True # 1 дублируется
#any_duplicates([[1, 2, 3], [3, 4, 5], [9, 8, 7]]) ➞ True # 3 дублируется

import random

# any_duplicates = ([[random.randint(1, 9)], [random.randint(1, 9)], [random.randint(1, 9)]])
e1 = [
    [1, 3, 2],
    [9, 7, 8],
    [4, 5, 6]
]
e2 = ([[1, 1, 3], [6, 5, 4], [8, 7, 9]])


def any_duplicates(square):
    available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in square:
        for number in row:
            try:
                available_numbers.remove(number)
            except ValueError:
                return True
    return False

any_duplicates(e2)