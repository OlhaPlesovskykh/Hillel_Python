"""
Запросить у пользователя 5 чисел и записать их в список
"""

list_1 = []
for i in range(1, 6):
    number = float(input(f"Введите число {i}: "))
    list_1.append(number)
print(list_1)
