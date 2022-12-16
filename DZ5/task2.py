"""
Вывести треугольник #2 с шириной N с помощью цикла while
"""

number = 1
width = int(input("Введите ширину треугольника - "))

while True:
    print("*" * number)
    number += 1

    if number > width:
        break
        