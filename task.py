# num = int(input('введите число '))
# if num %2 == 0:
#     print('четное число', num)
# else:
#     print('нечетное число')
#
# letter = input('input text')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('гласная буква')
# elif letter == 'y':
#     print('согласная и гласная')
# else:
#     print('согласная')

# num = int(input())
# data = []
# while num != 0:
#      data.append(num)
#      num = int(input())
# data.sort()
# print(data)

words = input()
data = []
while words != '':
    if words not in data:
        data.append(words)
    words = input()
print (data)

for item in data: # вытаскиваем элемент из массива
    print(item)