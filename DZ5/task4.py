"""
Вывести треугольник #4 с шириной N с помощью цикла while
"""

number = 1
width = int(input("Введите ширину треугольника - "))
space = width - 1

while True:
    print(" " * space + "*" * number)
    number += 1
    space -= 1
    
    if number > width:
        break
