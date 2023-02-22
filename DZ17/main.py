"""
Необходимо создать класс Human с атрибутами:
name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__
Так-же нужно написать методы:
get_info() - который возвращает словарь в котором находится информация о человеке
call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info
В качестве решения нужно отправить ссылку на GitHub репозиторий.
"""


class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        dict_info = {"name": self.name,
                     "surname": self.surname,
                     "age": self.age,
                     "phone": self.phone,
                     "address": self.address}
        return dict_info

    def call(self, phone_number):
        return f"{self.phone} вызывает абонента {phone_number}"


Person1 = Human("Olga", "Plesovskykh", 25, +38000000, "Odessa")
Person2 = Human("Sergey", "Plesovskykh", 33, +3800001, "Odessa")
Person3 = Human("Mike", "Plesovskykh", 2, +38000002, "Odessa")
print(Person1.get_info())
print(Person2.get_info())
print(Person3.get_info())
print(Person1.call(+38911111))
