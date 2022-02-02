"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера,
чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os


def project_dir(project_name, sub_folders):
    project_folder = os.path.join(os.getcwd(), project_name)

    if not os.path.exists(project_folder):
        os.mkdir(project_folder)

        for folder in sub_folders:
            path_to_make = os.path.join(project_folder, folder)
            os.mkdir(path_to_make)

            os.chdir(path_to_make)
            with open(f'base.html', 'w'), \
                    open(f'index.html', 'w'):
                pass

        print(f'Стартер проекта {project_name} создан.')

    else:
        print(f'Папка {project_name} уже существует. При отсутствии вложенных папок - они будут созданы.')

        for folder in sub_folders:

            if not os.path.exists(os.path.join(project_folder, folder)):
                path_to_make = os.path.join(project_folder, folder)
                os.mkdir(path_to_make)

                os.chdir(path_to_make)
                with open(f'base.html', 'w'), \
                        open(f'index.html', 'w'):
                    pass

                print(f'Вложенная папка {folder} создана.')

            else:
                path_to_make = os.path.join(project_folder, folder)

                os.chdir(path_to_make)
                with open(f'base.html', 'w'), \
                        open(f'index.html', 'w'):
                    pass

                    print(f'Папка {folder} существует, пропускаем.')
                    pass


project_name = 'my_project'
sub_folders = ['settings', 'mainapp', 'adminapp', 'authapp']

project_dir(project_name, sub_folders)







