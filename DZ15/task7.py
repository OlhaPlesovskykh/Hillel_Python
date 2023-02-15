"""
Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4
"""


with open('python.txt', 'r') as f:
    data = f.read().split()
word_list = []
[word_list.append((data.count(i), i)) for i in data if (data.count(i), i) not in word_list]
word_list.sort(reverse=True)
[print(f"{i[1]} - {i[0]} раз") for i in word_list[:5]]
