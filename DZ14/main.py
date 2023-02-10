def cache_decorator(func):
    """
    Данный Декоратор кеширует все запросы вызываемых функций
    В случае если функция вызывается первый раз,
    декоратор вызовет на выполнение функцию с указанными параметрами
    В случае если функция с заданными параметрами уже вызывалась,
    декоратор сразу вернёт закешированный результат
    :param func: Функция
    :return: Результат
    """
    test = {}
    test[func.__name__] = {}
    def inner(*args):
        for k, v in test.items():
            if args in v.keys():
                return v[args]
        result = func(*args)
        test[func.__name__][args] = result
        return result
    return inner


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    """
    Функция считает площадь треугольника
    :param a: Сторона треугольника
    :param b: Сторона треугольника
    :return: Площадь
    """
    print(f"Вызвана функция triangle_area с аргументами {a} и {b}")
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    """
    Функция считает площадь круга
    :param r: Радиус
    :return: Площадь
    """
    print(f"Вызвана функция circle_area с аргументом {r}")
    return 3.14 * (r * r)


print("Результат выполнения triangle_area(5, 10):", triangle_area(5, 10))
print("Результат выполнения triangle_area(5, 10):", triangle_area(5, 10))
print("Результат выполнения circle_area(20):", circle_area(20))
print("Результат выполнения circle_area(20):", circle_area(20))
print("Результат выполнения triangle_area(10, 10):", triangle_area(10, 10))
print("Результат выполнения triangle_area(5, 10):", triangle_area(5, 10))
