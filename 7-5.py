"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

{
    100: (15, ['txt']),
    1000: (3, ['py', 'txt']),
    10000: (7, ['html', 'css']),
    100000: (2, ['png', 'jpg'])
}

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""


import os
import json


def ext_dir_stats(dir_path):
    abs_path = os.path.abspath(dir_path)
    folder_name = abs_path.split('\\')[-1]

    size_bins = [100, 1000, 10000, 100000]
    files_dict = {k: [0, []] for k in size_bins }

    for i in os.listdir(abs_path):

        if os.path.isfile(i):

            file_size = os.stat(i).st_size
            extension = i.split('.')[-1]

            if 100 <= file_size < 1000:
                files_dict[100][0] += 1
                if extension not in files_dict[100][1]:
                    files_dict[100][1].append(i)

            elif 1000 <= file_size < 10000:
                files_dict[1000][0] += 1
                if extension not in files_dict[1000][1]:
                    files_dict[1000][1].append(i)

            elif 10000 <= file_size < 100000:
                files_dict[10000][0] += 1
                if extension not in files_dict[10000][1]:
                    files_dict[10000][1].append(i)

            elif file_size > 100000:
                files_dict[100000][0] += 1
                if extension not in files_dict[100000][1]:
                    files_dict[100000][1].append(i)
            else:
                pass

        else:
            pass

    files_dict = {k: tuple(v) for k, v in files_dict.items()}

    with open(f'{folder_name}_summary.json', 'w') as f:
        json.dump(files_dict, f, ensure_ascii=False)

    return files_dict

path = r'E:\Факультет Data engeneering\I четверть\2. Основы языка Python\Урок 7. ' \
       r'Работа с файловой системой. Исключения в Python\HW_7'

print(ext_dir_stats(path))
# out: {100: (2, ['config.yaml', 'HW_7_summary.json']), ...}

"""
В json сохраняет значения словарей не как кортежи а как списки, 
т.к. как я понял в формате json нет понятия кортеже.

Так же не очень доволен кодом, т.к. слишком много ветвлений и выглядит довольно громоздко, 
я уверен что можно было записать по компактнее. Если у вас есть рекомендация по этому поводу - дайте знать.

"""


