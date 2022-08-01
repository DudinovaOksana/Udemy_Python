#Написать игру в "камень-ножницы-бумага" против компьютера.
#Запустить игру в бесконечном цикле. Запросить ввод от пользователя
#(R - камень, S - ножницы, P - бумага). Сгенерировать случайный выбор
#компьютера. Вывести выбор компьютера. Определить победителя, выведя
#соответствующую информацию. Спросить пользователя - хочет ли он повторить игру.
#Если хочет - повторить, не хочет - выйти из цикла.

import random

list = ['rock', 'scissors', 'paper']
tries = 0
while True:

    users_choice = input("Enter rock or scissors or paper ")
    computer_choice = random.choice(list)
    print(computer_choice)
    tries

    if users_choice == computer_choice:
        print('Draw')
    elif users_choice == 'rock' and computer_choice == 'paper':
        print('User won')
    elif users_choice == 'scissors' and computer_choice == 'paper':
        print('User won')
    elif users_choice == 'paper' and computer_choice == 'rock':
        print('Computer won')
    elif users_choice == 'paper' and computer_choice == 'scissors':
        print('Computer won')
    elif users_choice == 'rock' and computer_choice == 'scissors':
        print('User won')
    elif users_choice == 'scissors' and computer_choice == 'rock':
        print('Computer won')
    new_game = input("Do you want repeat the game?")
    if new_game == "Yes":
        continue
    if new_game == "No":
        break