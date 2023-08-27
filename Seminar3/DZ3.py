# Задача 1 Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# # list_1 = [1, 2, 3, 4, 5]
# # k = 3
# # 1

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count_k = 0 
# for i in range(len(list_1)): 
#     if list_1[i]== k: 
#         count_k = count_k +1 
# print(count_k)



# Задача 2 Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

# Вариант1 с рандомом
# import random

# N = int(input("Введите количество элементов в массиве "))
# list = [random.randint(1, 20) for i in range(N)]
# print(list)
# x = int(input("Введите искомое число "))
# index_element = 0
# min_element = abs(x - list[0])
# for i in range(1, N):
#     buffer_element = abs(x -list[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = i

# print(f"Самый близкий по величине элемент к заданному числу {list[index_element]}")

# Вариант 2 с заданными параметрами
# list_1 = [1, 2, 3, 4, 5]
# k = 6

# N = len(list_1)
# index_element = 0
# min_element = abs(k - list_1[0])
# for i in range(1, N):
#     buffer_element = abs(k -list_1[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = i
# print(list_1[index_element])

# Вариант 3 с заданными параметрами эталонное решение с сайта
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)




# Задача 3 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# Вариант1 с вводом слова с клавиатуры
# import re 
# def Scrabble(text):
#     return bool(re.search("[а-яА-Я]", text))
# Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т",
#         2:"Д, К, Л, М, П, У",
#         3:"Б, Г, Ё, Ь, Я",
#         4:"Й, Ы", 
#         5:"Ж, З, Х, Ц, Ч", 
#         8:"Ш, Э, Ю",
#         10:"Ф, Щ, Ъ"} 
# Eng = { 1:"A, E, I, O, U, L, N, S, T, R ",
#         2:"D, G", 
#         3:"B, C, M, P", 
#         4:"F, H, V, W, Y", 
#         5:"K", 
#         8:"J, X"} 
# text = input("Введите слово: ").upper() 

# if Scrabble(text):
#     print(sum([a for i in text for a, v in Rus.items() if i in v])) 
# else: 
#     print(sum([a for i in text for a, v in Eng.items() if i in v]))

# Вариант 2 слово задано изначально 
# k = 'ноутбук'
# import re 
# def Scrabble(k):
#     return bool(re.search("[а-яА-Я]", k))
# Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т",
#         2:"Д, К, Л, М, П, У",
#         3:"Б, Г, Ё, Ь, Я",
#         4:"Й, Ы", 
#         5:"Ж, З, Х, Ц, Ч", 
#         8:"Ш, Э, Ю",
#         10:"Ф, Щ, Ъ"} 
# Eng = { 1:"A, E, I, O, U, L, N, S, T, R ",
#         2:"D, G", 
#         3:"B, C, M, P", 
#         4:"F, H, V, W, Y", 
#         5:"K", 
#         8:"J, X"} 
# k = k.upper()

# if Scrabble(k):
#     print(sum([a for i in text for a, v in Rus.items() if i in v])) 
# else: 
#     print(sum([a for i in text for a, v in Eng.items() if i in v]))

# Вариант3 слово задано изначально, образец решения на сайте
# k = 'ноутбук'
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)