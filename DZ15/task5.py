"""
Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
"""


with open('text.txt', 'r') as f:
    data = f.read().split()
    print(len(data))
    