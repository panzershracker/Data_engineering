"""
3. Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
...
    |--templates
    |   |--mainapp
    |   |  |--base.html
    |   |  |--index.html
    |   |--authapp
    |      |--base.html
    |      |--index.html

Примечание: исходные файлы необходимо оставить;
обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
"""

import shutil, os


def move_subfolders(path_from, foder_name):
    subdirs_list = os.listdir(path_from)

    new_dir = os.path.join(path_from, foder_name)

    if not os.path.exists(new_dir):

        shutil.copytree(path_from, new_dir)

        for i in subdirs_list:
            shutil.rmtree(os.path.join(path_from, i))

        print('Готово!')

    else:
        print('Папка уже существует!')

move_subfolders(r'my_project', r'templates')

