"""
Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
"""


with open('numbers.txt', 'r') as f:
    numbers = map(float, f.read().split())
    print(sum(numbers))
    