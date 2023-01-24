"""
Дано два множества A и B
В множестве А находятся имена должников за Сентябрь
В множестве B находятся имена должников за Октябрь
Найти:
* Вывести имена людей которые должны за Сентябрь и Октябрь
* Вывести должников за Октябрь у которых нет долга за Сентябрь
"""

A = {'Irina', 'Oleg', 'Alexander', 'Oscar', 'Maria', 'Denis', 'Alice', 'Roman', 'Diana'}
B = {'Olha', 'Maria', 'Oscar', 'Mike', 'Paul', 'Roman', 'John'}

credit_September_and_October = A | B
print(f"Должники за Сентябрь и Октябрь: {credit_September_and_October}")

credit_October_only = B - A
print(f"Должники за Октябрь у которых нет долга за Сентябрь: {credit_October_only}")
