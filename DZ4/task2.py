"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max
"""

a = float(input("Введите число a - "))
b = float(input("Введите число b - "))
c = float(input("Введите число c - "))

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
else:
    max = c
print(max)
