# Задание 16.9.1
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}'
rez = Rectangle(5,10,50,100)
print(rez)

# Задание 16.9.2
class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

# Метод расчитывающий площадь
    def getArea(self):
        return self.width * self.height

rect_1 = Rectangle(3,4)
print(rect_1.getArea())

# Задание 16.9.3
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname} . {self.city}. Баланс: {self.balance} руб.'
client_1 = Client('Иван', 'Петров', 'Москва', 50)
print(client_1)

# Задание 16.9.4
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname} . {self.city}. Баланс: {self.balance} руб.'
    def guest(self):
        return f'{self.name} {self.surname} . {self.city}.'
client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Петр', 'Иванов', 'Тула', 35)
client_3 = Client('Вася', 'Сидоров', 'Тверь', 55)

client_list = [client_1, client_2, client_3]
for guest in client_list:
    print(guest.guest())




