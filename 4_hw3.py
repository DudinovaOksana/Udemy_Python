#Играем в кости.Правила следующие:
#1.Кидаем пару костей.
#2.Складываем количество выпавших чисел и прибавляем к общему
#кол - ву очков
#3. Повторяем пункты 1 и 2 трижды.
#4.Если выпадает дуплет(на обоих костях одно и то же число), то
#кол - во очков обнуляется и последующие броски не считаются.
#Задание: Напишите функцию calc_dice_scores принимающую список
#кортежей и, возвращающую общее кол - во очков.
#Примеры вызовов и ожидаемый результат.
#calc_dice_scores([(1, 2), (3, 4), (5, 6)]) ➞ 21
#calc_dice_scores([(1, 1), (5, 6), (6, 4)]) ➞ 0
#calc_dice_scores([(4, 5), (4, 5), (4, 5)]) ➞ 27
#Всегда передаются три кортежа по два элемента в каждом.

# import random
#
#
# all_throws = [(random.randint(1, 6), random.randint(1, 6)),
#               (random.randint(1, 6), random.randint(1, 6)),
#               (random.randint(1, 6), random.randint(1, 6))]
#

def calc_dice_scores(lst: list) -> int:
    score = 0
    for i in lst:
        n, m = i
        if n == m:
            score = 0
            break
        else:
            score = score + n + m
    return score

# print(all_throws)
# s = calc_dice_scores(all_throws)
# print(f'Score: {s}')