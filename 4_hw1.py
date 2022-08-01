#Два участника p1 и p2 участвуют в дуэли.
#Напишите функцию whos_first, которая принимает две строки
#и возвращает имя игрока, который выстрелил первым.
#Если игроки выстрелили одновременно, то вернуть строку "tie".
#Примеры вызовов и возвратов:
#whos_first(
# "   Bang!        ",
# "        Bang!   "
#) ➞ "p1"
# p1 стреляет быстрее p2
#whos_first(
# "               Bang! ",
# "             Bang!   "
#) ➞ "p2"
#whos_first(
# "     Bang!   ",
# "     Bang!   "
#) ➞ "tie"
#Примечание:передаваемые строки - могут быть различной длины!
# (то есть содержать различное количество пробелов)

import random

space1 = (random.randint(0, 14)) * ' '
space_1 = (random.randint(0, 14)) * ' '
p1 = space1 + "Bang!" + space_1
space2 = (random.randint(0, 14)) * ' '
space_2 = (random.randint(0, 14)) * ' '
p2 = space2 + "Bang!" + space_2


def whos_first(p1, p2):
    print(p1)
    print(p2)
    if space1 > space2:
        print('p2 won')
    elif space1 < space2:
        print('p1 won')
    elif space1 == space2:
        print('tie')


whos_first(p1, p2)