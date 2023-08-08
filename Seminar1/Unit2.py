# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

students1 = int(input('Введите кол-во учеников в 1 классе: '))
students2 = int(input('Введите кол-во учеников в 2 классе: '))
students3 = int(input('Введите кол-во учеников в 3 классе: '))

desks1 = (students1 - 1) // 2 + 1
desks2 = (students2 - 1) // 2 + 1
desks3 = (students3 - 1) // 2 + 1
res = desks1 + desks2 + desks3

print('Минимальное число парт для оборудования трех кабинетов равно', res)
