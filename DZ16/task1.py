"""
Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк
"""
import pickle


list_of_dicts = [{"A": "test"}, {"A": "test2"}, {"A": "test3"}]
with open("test.bin", "wb") as file:
    pickle.dump(list_of_dicts, file)
