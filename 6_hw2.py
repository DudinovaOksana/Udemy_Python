#Создайте класс Calculator который поддерживает: сложение двух чисел
#вычисление разницы между двумя числами умножение двух чисел
#деление одного числа на другое
#Примеры вызовов и возвратов из функций:
#calculator = Calculator()
#calculator.add(10, 5) ➞ 15
#calculator.subtract(10, 5) ➞ 5
#calculator.multiply(10, 5) ➞ 50
#calculator.divide(10, 5) ➞ 2

class Calculator:

    def add(self, a, b):
        return a+b

    def subtract(self, a,b):
        return a-b

    def multiply(self, a,b):
        return a*b

    def divide(self, a,b):
        return a/b

c = Calculator()
print(c.add(10, 5))
print(c.subtract(10,5))
print(c.multiply(10,5))
print(c.divide(10,5))
print(Calculator.add(1,2))