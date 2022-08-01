#На вход подаются два списка чисел длины N.
#Задача: взять из первого списка все нечётные числа,
# из второго чётные и объединить их в новом списке с названием
# joined_list.
#Примечание: можно сделать двумя циклами for, можно одним, можно
# с помощью list comprehensions.
import sys
first_lst = sys.argv[1].split(',')
second_lst = sys.argv[2].split(',')

joined_list = []

for i in first_lst:
    if int(i) % 2 != 0:
        joined_list.append(i)
for i in second_lst:
    if int(i) % 2 == 0:
        joined_list.append(i)
print(joined_list)