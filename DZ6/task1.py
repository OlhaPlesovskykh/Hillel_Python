"""
Программа запрашивает у пользователя пароль и записывает в переменную password.

Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке, максимальное количество баллов - 5

Проверки:

Длина пароля больше или равно 8 символам
В пароле есть хотя бы одна цифра
В пароле есть хотя бы одна большая
В пароле есть хотя бы одна маленькая буква
В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же рекомендации по улучшению пароля.
"""

password = input("Enter your password: ")
len_string = 0
has_digit = 0
has_upper = 0
has_lower = 0
has_spec = 0

if len(password) >= 8:
    len_string = 1

for char in password:
    if char.isdigit():
        has_digit = 1
    if char.isupper():
        has_upper = 1
    if char.islower():
        has_lower = 1
    if not char.isalnum():
        has_spec = 1

score = len_string + has_digit + has_upper + has_lower + has_spec
print(f"Password score: {score}")

if not len_string or not has_digit or not has_upper or not has_lower or not has_spec:
    print("Recommendation:")

if not len_string:
    print("The minimum password length is 8")

if not has_digit:
    print("Use digits")

if not has_upper:
    print("Use capital letters")

if not has_lower:
    print("Use lowercase letters")

if not has_spec:
    print("Use special characters")
