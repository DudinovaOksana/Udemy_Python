#Создайте класс Circle который конструируется с передачей радиуса в качестве аргумента.
#Класс Circle должен предоставлять две функции:
#get_area, которая возвращает площадь круга
#get_perimeter, которая возвращает длину окружности
# Примеры вызовов
#circle = Circle(10)
#area = circle.get_area()  # возвращает 314.1592653589793
#perimeter = circle.get_perimeter()  # возвращает 62.83184

class Circle:
    def __init__(self, radius):
        self.radius=radius

    def get_area(self):
        return 3.1415926535897*(self.radius**2)

    def get_perimeter(self):
        return 2*3.141592*self.radius

circle=Circle(10)
area=circle.get_area()
perimeter=circle.get_perimeter()
print(area)
print(perimeter)