"""
Дано два словаря
A = {'key': 1}
B = {'key1: 2}
Необходимо написать код который будет их объединять
C = {'key': 1, 'key1': 2}
Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы не потерять значения
нужно записать в один ключ список в котором будут находится значения
Например:
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = {'key': [1, 'Hello'], 'key2': True}
Записать результат в файл result.json в формате JSON.
В качестве решения отправить ссылку на github репозиторий.
"""


def update_dict(current_dct: dict, new_object: dict) -> dict:
    """
    Function is fill in dictionary, verify if new object key is already exist
    in current dictionary.
    If new object key is already exist in current dictionary, Function will merge
    value from old object key with value from object new key in list format
    :param current_dct: current dictionary
    :param new_object: new object that will be added to current dictionary
    :return: updated dictionary
    """
    for new_key, new_value in new_object.items():
        if new_key in current_dct:
            if isinstance((current_dct[new_key]), list):
                current_dct[new_key].append(new_value)
            else:
                current_dct[new_key] = [(current_dct[new_key]), new_value]
        else:
            current_dct.update(new_object)
        return current_dct


A = {"key": 1}
B = {"key1": 2}
C = {"key": "Hello"}
F = {"key": "Hello4"}
Q = {"key1": "333"}
D = {}
[update_dict(current_dct=D, new_object=obj) for obj in [A, B, C, F, Q]]
print(D)  # {'key': [1, 'Hello', 'Hello4'], 'key1': [2, '333']}
