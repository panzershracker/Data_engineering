"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:

{
    100: 15,
    1000: 3,
    10000: 7,
    100000: 2
}

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os


def dir_stats(dir_path):
    abs_path = os.path.abspath(dir_path)

    size_bins = [100, 1000, 10000, 100000]
    files_dict = {k:0 for k in size_bins }

    for i in os.listdir(abs_path):

        if os.path.isfile(i):

            if 100 <= os.stat(i).st_size < 1000:
                files_dict[100] += 1
            elif 1000 <= os.stat(i).st_size < 10000:
                files_dict[1000] += 1
            elif 10000 <= os.stat(i).st_size < 100000:
                files_dict[10000] += 1
            elif os.stat(i).st_size > 100000:
                files_dict[100000] += 1
            else:
                pass

        else:
            pass

    return files_dict

path = r'E:\Факультет Data engeneering\I четверть\2. Основы языка Python\Урок 7. ' \
       r'Работа с файловой системой. Исключения в Python\HW_7'

print(dir_stats(path))
# out: {100: 2, 1000: 4, 10000: 0, 100000: 0}

