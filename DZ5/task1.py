"""
Вывести треугольник #1 с шириной N с помощью цикла while
"""

width = int(input("Введите ширину треугольника - "))
while True:
    print("*" * width)
    width -= 1

    if width < 1:
        break
