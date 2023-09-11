# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Пример ввода
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)

# Вариант 1   из интернета
# def check_values(x, y):
#     if x == y:
#         return print('Равны')
#     return print('Не равны')

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation = lambda x: x
# transormed_values = list(map(transformation, values))

# check_values(values, transormed_values)

# Вариант 2 через лямбда функцию решено на семинаре
# transformation = lambda el: el
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Пример ввода
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вариант 1 из инета
# def find_farthest_orbit(list_of_orbits):
#     max_orbit = 0
#     list_s_orbits = [0, 0]
#     for i in range(len(list_of_orbits)):
#         a, b = list_of_orbits[i]
#         if a != b:
#             s = 3.14 * a * b
#             if s > max_orbit:
#                 max_orbit = s
#                 list_s_orbits[0] = a
#                 list_s_orbits[1] = b
#     return set(list_s_orbits)


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(find_farthest_orbit(orbits))
# print(max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1]))

# Вариант 2 решено на семинале
# def find_farthest_orbit(list_of_orbits):
#     smax= 0
#     max_x_y = 0 
#     for x,y in list_of_orbits: 
#         if x!=y: 
#             s=x*y
#             if s > smax:
#                 smax=s
#                 max_x_y = (x,y)
#     return max_x_y
	
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Пример ввода
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristics, objects):
#     filtered = filter(characteristics, objects)
#     filteredList =     list(filtered)           
#     if len(filteredList) == len(objects) or len(filteredList) == 0:
#         return True
#     return False

# values = [1, 3, 9, 7, 2]


# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")