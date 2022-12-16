"""
Вывести треугольник #3 с шириной N с помощью цикла while
"""

space = 0
width = int(input("Введите ширину треугольника - "))
while True:
    print(' ' * space + "*" * width)
    width -= 1
    space += 1

    if width < 1:
        break
