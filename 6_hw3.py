#Создать класс Employee, который принимает имя, фамилию и зарплату в качестве аргументов при конструировании.
#Класс должен поддерживать:
#атрибут first_name, возвращающий имя
#атрибут last_name, возвращающий фамилию
#атрибут salary, возвращающий зарплату
#функцию from_string, которая принимает имя, фамилию и зарплату в формате 'first_name-last_name-salary',
#парсит строку и возвращает экземпляр Employee
#Примеры
#emp1 = Employee('Mary', 'Sue', 60000)
#emp2 = Employee.from_string('John-Smith-55000')
#emp1.first_name ➞ 'Mary'
#emp1.salary ➞ 60000
#emp2.first_name ➞ 'John'
#emp2.salary ➞ 55000

class Employee:
    def __init__(self,f, l, s):
        self.first_name=f
        self.last_name=l
        self.salary=s

    @staticmethod
    def from_string(string_name):
        string_list = string_name.split('-')
        return Employee(string_list[0], string_list[1], int(string_list[2]))

    def b(self, f):
        return self.first_name+f


emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')
print(emp2.last_name)
print(emp2.b('g'))
def g(b):
    return b+1