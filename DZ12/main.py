"""
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
"""

number_of_files = int(input("Введите количество файлов: "))
list_of_files_with_permissions = []
list_of_target_operations = []
dict_of_files = {}
dict_of_operationas = {}

for _ in range(number_of_files):
    list_of_files_with_permissions.append(input("Введите название файла и допустимые операции: "))

for item in list_of_files_with_permissions:
    current_file = item.split()
    permissions_list = []
    if "R" in current_file[1:]:
        permissions_list.append("read")
    if "W" in current_file[1:]:
        permissions_list.append("write")
    if "X" in current_file[1:]:
        permissions_list.append("execute")
    dict_of_files[current_file[0]] = permissions_list

number_of_operations = int(input("Введите количество операций: "))
for _ in range(number_of_operations):
    list_of_target_operations.append(input("Введите операцию и имя файла: "))

for item in list_of_target_operations:
    current_operation = item.split()
    dict_of_operationas[current_operation[1]] = current_operation[0]

for item in dict_of_operationas:
    if dict_of_operationas[item] in dict_of_files[item]:
        print("OK")
    else:
        print("Access denied")
