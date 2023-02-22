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
    test = {func.__name__: {}}

    def inner(*args, **kwargs):
        kwargs.update(zip(func.__code__.co_varnames, args))
        sorted_tuple = tuple(sorted(kwargs.values(), key=lambda x: x))
        if sorted_tuple in test[func.__name__]:
            return test[func.__name__][sorted_tuple]
        result = func(**kwargs)
        test[func.__name__][sorted_tuple] = result
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


print("Результат выполнения triangle_area(5, 10):", triangle_area(a=5, b=10))
print("Результат выполнения triangle_area(5, 10):", triangle_area(b=10, a=5))
print("Результат выполнения circle_area(20):", circle_area(20))
print("Результат выполнения circle_area(20):", circle_area(20))
print("Результат выполнения triangle_area(10, 10):", triangle_area(10, 10))
print("Результат выполнения triangle_area(5, 10):", triangle_area(5, 10))
"""
Вызвана функция triangle_area с аргументами 5 и 10
Результат выполнения triangle_area(5, 10): 50
Результат выполнения triangle_area(5, 10): 50
Вызвана функция circle_area с аргументом 20
Результат выполнения circle_area(20): 1256.0
Результат выполнения circle_area(20): 1256.0
Вызвана функция triangle_area с аргументами 10 и 10
Результат выполнения triangle_area(10, 10): 100
Результат выполнения triangle_area(5, 10): 50
"""