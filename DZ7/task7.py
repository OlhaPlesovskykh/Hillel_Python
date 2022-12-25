"""
Пользователь вводит текст нужно вывести количество цифр в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество цифр: 7
"""

text = input("Введите текст: ")
list_of_numbers = []
for i in text:
    if i.isdigit():
        list_of_numbers.append(i)
print(f"Количество цифр: {len(list_of_numbers)}")
