# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# list_n = list()
# amount_list_n = int(input("Введите желаемое кол-во элементов в первом списке: "))

# for i in range(amount_list_n):
#     list_n.append(int(input("Введите значения для первого списка: ")))

# list_m = list()
# amount_list_m = int(input("Введите желаемое кол-во элементов во втором списке: "))

# for i in range(amount_list_m):
#     list_m.append(int(input("Введите значения для второго списка: ")))

# list_n = set(list_n)
# list_m = set(list_m)

# result_list = list(list_n.intersection(list_m))
# result_list.sort()
# print(result_list)




# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с
# двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.



# n = int(input("Введите кол-во кустов: "))
# number_of_berries = []
# i = 0

# while i in range(n):
#     number_of_berries.append(int(input("Введите количество ягод на кусте {num_berry_bush}: ".format(num_berry_bush = i + 1))))
#     i += 1

# max_number_of_berries = 0
# max_number_of_berries_pos = 0
# cur_res = 0
# i = 0

# while i in range(n):
#     if i == 0:
#         prew_index = len(number_of_berries) - 1
#     else:
#         prew_index = i - 1
#     if i == len(number_of_berries) - 1:
#         next_index = 0
#     else:
#         next_index = i + 1

#     cur_res = number_of_berries[prew_index] + number_of_berries[i] + number_of_berries[next_index]

#     if cur_res > max_number_of_berries:
#         max_number_of_berries = cur_res
#         max_number_of_berries_pos = i + 1
#     i += 1

# print(max_number_of_berries)


