"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...


@type_logger
def calc_cube(x):
    return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


from functools import wraps


def type_logger(invis=False):
    def _type_logger(func):
        @wraps(func)
        def wrapper(*args):
            calc = func(*args)

            if invis:
                pass
            else:
                args_list = [f'{i}: {type(i)}' for i in args]
                print(f'{func.__name__}({args_list})')

            return calc

        return wrapper

    return _type_logger


@type_logger(invis=False)
def calc_cube(*args):

    for i in args:
        yield i ** 3


result = calc_cube(3, 5)

print(*result)
# out: calc_cube(["3: <class 'int'>", "5: <class 'int'>"])
#      27 125

print(calc_cube.__name__)
# out: calc_cube


"""
Верно ли я понял, что под маскировкой понимался @wraps?
По поводу именнованных аргументов - не сообразил как сделать. Подскажите пожалуйста.
Возможно так же как я делал но с генератором словаря...
"""



