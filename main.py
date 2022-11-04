# first_name = input("Введите ваше имя:")
# last_name = input("Введите вашу фамилию:")
# age = input("Введите ваш возраст:")
# city = input("Введите город проживания:")

# Выводим пустую строку
# print("")
#
# # Выводим приветствие, подставляя имя и фамилию пользователя,
# # которые он ввел с клавиатуры
# print("Привет,", first_name, last_name, "!")
#
# # Выводим пустую строку
# print("")
#
# # Выводим фиксированный текст для удобства просмотра
# print("Ваш профиль:")
#
# # Выводим возраст и город, которые указал пользователь
# print("Возраст:", age)
# print("Город:", city)

# print(3 > 10)
# # False
#
# print(3 < 10)
# # True
#
# print(3 == 10) # равны ли объекты?
# # False
# print('r' in 'world') # проверяем отдельный символ
# # True
#
# print('th' in 'python') # проверяем целую подстроку
# # True
#
# print('the' in 'python')
# # False
#
# date = (1, 'january', 2020)
# print(date[0])
# # 1
# print(date[1])
# # january
# print(date[2])
# # 2020
#
# s1 = "foo"
# s2 = "bar"
# s1 = s1+s2
# print(s1)
# # foobar
# s1 = "foo"
# print(id(s1), s1) #проверяем идентификатор
# # 139953609727144, foo
#
# s2 = "bar"
# print(id(s2), s2) #проверяем идентификатор
# # 139953609727088, bar
#
# s1 = s1+s2
# print(id(s1), s1) #проверяем идентификатор
# # 139953459591296, foobar

# colors = 'red green blue'
# colors_split = colors.split() # список цветов по отдельности
#
# colors_joined = ' and '.join(colors_split) # объединение строк
# print(colors_joined)

# numbers = input("Введите числа через пробел:")
#
# numbers_split = numbers.split()
# numbers_lines = "\n".join(numbers_split)
#
# print(numbers_lines)

# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
#
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка


# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
L = list(map(float, input().split()))

# обмениваем первое и последнее число
# с помощью множественного присваивания
L[0], L[-1] = L[-1], L[0]

# находим сумму и добавляем её в конец списка
L.append(sum(L))

print(L)