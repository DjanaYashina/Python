# Задача №31. 
# Последовательностью Фибоначчи называется последовательность чисел a0,
# a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def find_nth_fib(n):
#     if n in [1, 2]:
#         return 1
#     return find_nth_fib(n - 1) + find_nth_fib(n - 2)
# print (find_nth_fib(7))


# Задача №33. 
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def input_number(msg: str):
#     while True:
#         num = input(msg)
#         if num.isdigit():
#             num = int(num)
#             return num

# amount = input_number("Enter amount of grades you want to input: ")
# grades = [] # list()

# for _ in range(amount):
#     user_input = input_number("Enter a grade: ")
#     grades.append(user_input)

# def max_to_min(arr: list):
#     max_num = max(arr)
#     min_num = min(arr)
#     for i in range(len(arr)):
#         if arr[i] == max_num:
#             arr[i] = min_num
        
# max_to_min(grades)
# print(grades)

# Задача №35. 
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
# Input: 5
# Output: yes 

# def prime(n):
#     for div in range(2, int(n**0.5)+1): #int(n**0.5)+1 - так обозначается корень из n, а +1 чтобы в рейнже включалось число
#         if n%div == 0:
#             return "Not Prime"
#     return "Prime"

# num = int(input("Введите число: "))

# print(prime(num))



# Задача №37 
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

# def pr_reverse(n):
#     if n == 0:
#         return ''
#     k = int(input())  # либо k = input()
#     return pr_reverse(n - 1) + ' ' + str(k) # либо eturn pr_reverse(n - 1) + ' ' + k
# num = 5
# print(pr_reverse(num))

# def print_reversed(amount: int):
#     if amount == 0:
#         return ""
#     num = input("Enter a number: ")
#     return f"{num} {print_reversed(amount - 1)}".rstrip()[::-1]