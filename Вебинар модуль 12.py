# name = 'Ivan'
# # camel case
# userName = 'Tom'
# user_name = 'Kate'

# Data Types
# name = input('Введите название книги')
# author = input('Введите фамилию автора')
# year = int(input('Введите год выпуска'))
# book = {'Название': name, 'Автор': author, 'Год выпуска': year}
# print(book)

text = input("Введите текст:")

unique = list(set(text))

print("Количество уникальных символов: ", len(unique))

# a = input("Введите первую строку чисел: ")
# b = input("Введите вторую строку чисел: ")
# a_1 = set(a)
# b_1 = set(b)
#
# a_and_b = a_1.symmetric_difference(b_1)
#
# print(a_and_b)

# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# print(id(a))
# print(id(b))
