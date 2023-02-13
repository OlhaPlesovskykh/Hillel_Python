"""
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. В исходном списке минимум 2 элемента.
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. Предполагается,
что элементы списка будут соответствовать правилам задания ключей в словарях.
Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно. Если пользователь задаст первое число большее чем второе,
просто поменяйте их местами.
"""


def change(current_list: list) -> list:
    if len(current_list) > 1:
        current_list[-1], current_list[0] = current_list[0], current_list[-1]
    return current_list


def to_dict(current_list: list) -> dict:
    current_dict = {i: i for i in current_list}
    return current_dict


def sum_range(start: int, end: int) -> int:
    number_sum = 0
    if start > end:
        start, end = end, start
    return sum([number_sum + i for i in range(start, end + 1)])


list_1 = [1, 2, 3]
print(change(list_1))
print(to_dict(list_1))
print(sum_range(1, 5))
