"""
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
"""


import random
open("random_numbers.txt", "w").close()
for i in range(100):
    with open("random_numbers.txt", "a") as f:
        f.write(str(random.randint(0, 9)) + "\n")
