
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
deposit = []
for value in per_cent:
    deposit.append(round((per_cent[value] * money / 100), 2))
print('deposit = ', deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max_deposit)






