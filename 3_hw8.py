import random

number = random.randint(1, 50)

count=1
while count<7:
    giving_number = int(input('Enter the number from 1 to 50'))
    if number==giving_number:
        print('You guessed the number!')
        break
    elif number>giving_number:
        print('You are wrong. Your number is greater')
    elif number<giving_number:
        print('You are wrong. Your number is less')
    count+=1









# if giving_number == number:
#     print('Вы угадали!')
# while giving_number != number:
#     print('Вы неугадали!')
#     if giving_number > number:
#         print('Введеное число число больше загаданного.')
#     if giving_number < number:
#         input("Введите снова число")


