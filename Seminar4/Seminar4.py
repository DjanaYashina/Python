# Задача №25. 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

#Вариант1 с использованием словоря букв
# string = "a a a b c a a d c d d"
# string_2 = string.split()
# dict = {}
# result = ""

# for i in range(len(string_2)):
#     if string_2[i] not in dict.keys():
#         dict[string_2[i]] = 1
#         result += f"{string_2[i]} "
#     else:
#         result += f"{string_2[i]}_{dict[string_2[i]]} "
#         dict[string_2[i]] += 1
# print(result)

#Вариант2 с использованием дополнительного листа и счетчика
# str = "a a a b c a a d c d d"
# my_list = str.split()
# letters = list()
# for i in range(len(my_list)):
#     if my_list[i] not in letters:
#         letters.append(my_list[i])
#     else:
#         letters.append(my_list[i])
#         my_list[i] += f"_{letters.count(my_list[i])-1}"
# print(" ".join(my_list))

# Задача №27. 
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# Вариант1
# text = '''She sells sea shells on the sea shore The shells that she sells are sea shells
#        I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells
#        are sea shore shells'''

# text_1 = text.replace(".", " ")
# text_2 = text_1.strip(".,!?\n").lower().split()
# print(f"В данном отрывке {len(text_2)} слов из них {len(set(text_2))} различных.")

# Вариант2
# user_input = "She sells sea shells on the sea shore The shells \
# that she sells are sea shells I'm sure. So if she sells sea \
# shells on the sea shore I'm sure that the shells are sea \
# shore shells"
# # example output: 19

# list_input = user_input.split() # сплит делит строку на элементы, если в сплит не указать разделители, то автоматом учитывается пробел

# for i in range(len(list_input)):
#     list_input[i] = list_input[i].lower()
#     if list_input[i][-1] in [".", ",", "!", "?"]:
#         list_input[i] = list_input[i][:len(list_input[i]) - 1]

# unique_words = set(list_input)
# print(len(unique_words))

# Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:                           Петя:
# n = int(input())                n = int(input())
# max_number = 1000               max_number = -1
# while n != 0:                   while n < 0:
#     n = int(input())                n = int(input())
#     if max_number > n:              if max_number < n:
#         max_number = n                  n = max_number
# print(max_number)               print(n)

# Решение:
# n = int(input())                  n = int(input())
# max_number = n                    max_number = n
# while n != 0:                     while n > 0:
#     n = int(input())                  n = int(input())
#     if max_number < n:                if max_number < n:
#         max_number = n                    max_number = n
# print(max_number)

# n = int(input("Enter a number: "))
# max_number = n
# while n > 0:
#     n = int(input("Enter a number: "))
#     if max_number < n:
#         max_number = n
# print(max_number)