"""
1. Создайте супер класс Shape и его наследников Triangle, Rectangle.
2. Класс Shape содержит абстрактный метод draw
3. Класс Triangle в инициализаторе принимает параметр width: int - ширина треугольника и реализует метод draw
(Выводит в консоль треугольник с шириной width)
4. Класс Rectangle в инициализаторе принимает параметр width: int и height: int - ширина, высота прямоугольника и
реализует метод draw (Выводит в консоль прямоугольник с шириной width и высотой height)
5. Создайте список с этими фигурами и в цикле вызовите метод draw у этих обьектов
P.S. Треугольник может быть любой (Равносторонний, Равнобедренный, Разносторонним) главное чтобы состоял и был заполнен
символом '*'.
Прямоугольник тоже должен состоять и быть заполнен символом '*'.
Важно: Используйте аннотации!
В качестве решения нужно отправить ссылку на github репозиторий."""


from abc import ABC


class Shape(ABC):
    def draw(self) -> None:
        pass


class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width

    def draw(self) -> None:
        number = 1
        while True:
            print("*" * number)
            number += 1
            if number > self.width:
                break


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self) -> None:
        for i in range(self.height):
            print("*" * self.width)


triangle = Triangle(10)
rectangle = Rectangle(5, 10)
figures = [triangle, rectangle]
for figure in figures:
    print("-------")
    figure.draw()
