#Построить цикл от 0 до введённого числа (включительно) и посчитать сумму всех чисел,
# делимых без остатка на 3 или 5. Вывести на консоль это число.
#Примечание: задача решается как прямым for, так и с помощью list comprehension
#(просуммировать числа "профильтрованного" списка можно, передав список в функцию sum(arg_list)).
limit = int(input("Введите число: "))
# my_list = []
sum = 0
for i in range(limit + 1):
    if i%3==0 or i%5==0:
        sum = sum + i
    # if i % 3 == 0 and i <= x:
    #     my_list.append(i)
print("Result: ", sum)

