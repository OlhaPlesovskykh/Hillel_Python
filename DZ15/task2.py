"""
Запросить у пользователя текст и записать его в файл data.txt
"""


text = input("Input your text: ")
with open('data.txt', 'w') as f:
    f.write(text)
