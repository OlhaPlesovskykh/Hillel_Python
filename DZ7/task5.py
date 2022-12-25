"""
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""

A = []
C = []
for i in range(1, 6):
    number = float(input(f"Введите число {i}: "))
    A.append(number)
    if number > 5:
        C.append(number)
print(C)
