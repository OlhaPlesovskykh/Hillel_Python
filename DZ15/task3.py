"""
Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
"""


try:
    count_of_numbers = int(input("Input number count: "))
    open("numbers.txt", "w").close()
except ValueError:
    count_of_numbers = 0
    print("Wrong input, need type int")
try:
    for i in range(count_of_numbers):
        number = float(input(f"Input number {i + 1}: "))
        with open('numbers.txt', 'a') as f:
            f.write(str(number) + " ")
except ValueError:
    print("Wrong input, need type int or float")
