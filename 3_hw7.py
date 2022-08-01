#На вход подаётся число. Определить является ли оно палиндромом.
#Число является палиндромом если прочитанное справа налево равно исходному числу.
#Примеры:
#121 - палиндром
#222 - палиндром
#321 - не палиндром
#1212 - не палиндром
#12121 - палиндром и так далее...
#Важное требование:  запрещается исходное число конвертировать в строку и применять к ней функцию реверсирования.
#Проверку требуется проводить применяя математические операции к исходному числу!
#Подсказки:
#number % 10 позволяет взять цифру последнего разряда
#number * 10 позволяет добавить разряд к числу
#number // 10 позволят отрезать последний разряд от числа
#Если число является палиндромом, вывести на консоль 'Palindrome', иначе вывести 'No Palindrome'.

number = 123321
# if str(number) == str(number)[::-1]:
#      print("This string is a palindrom")
# else:
#     print("This string is not a palindrom")

# r = 0
# while r < number:
#     r = int(10 * r + number % 10)
#     number = number // 10
# if (number == r) or (number == int(r / 10)):
#     print("Palindrome")
# else:
#     print("No Palindrome")

reversed_number=0
tmp_original=number
while tmp_original>0:
    reversed_number=(reversed_number*10)+tmp_original%10
    tmp_original=tmp_original//10
if number==reversed_number:
    print('Palindrome')
else:
    print('Palindrome')
