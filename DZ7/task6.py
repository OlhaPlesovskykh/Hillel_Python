"""
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
"""

N = int(input("Введите число N: "))
A = []
for i in range(1, N + 1):
    number = int(input(f"Введите число {i}: "))
    A.append(number)
min_value = A[0]
max_value = A[0]
for i in A:
    if min_value > i:
        min_value = i
    elif max_value < i:
        max_value = i
print(f"Минимальное число: {min_value}, Максимальное число: {max_value}")
