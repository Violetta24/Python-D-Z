# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input("Введите число: "))
# b = int(input("В какую степень возвести число: "))


# def raise_degree(a, b):
#     if b == 1:
#         return a
#     if b != 1:
#         return a * raise_degree(a, b - 1)


# print(raise_degree(a, b))




# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

# A = int(input("a :"))
# B = int(input("b :"))
# def sum(A, B):
#     if A == 0:
#         return B
#     return sum(A - 1, B + 1)
# print(sum(A,  B))