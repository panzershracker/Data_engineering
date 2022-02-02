"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
"""
import os
import sys
import itertools
import json


def user_hobbies(users_file, hobby_file):

    with open(users_file, encoding='utf-8') as users, \
            open(hobby_file, encoding='utf-8') as hobby:

        users_len = sum(1 for i in open('users.csv', encoding='utf-8'))
        hobby_len = sum(1 for i in open('hobby.csv', encoding='utf-8'))

        if users_len >= hobby_len:
            result = {k.rstrip().replace(',', ' '): v.rstrip() for k, v in
                      itertools.zip_longest(users, hobby, fillvalue='None')}

        else:
            sys.exit(1)

    with open('prompt_app.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)

    print('Готово! Файл "prompt_app.json" создан')


if __name__ == '__main__':

    path_1 = os.path.abspath(input('Введи путь к файлу users\n'))
    path_2 = os.path.abspath(input('Введи путь к файлу hobby\n'))

    user_hobbies(path_1, path_2)


""" 
Ох и намучался я с этими путями в windows )))!
Целый день убил на это задание, но проблемы было только две:
1. пути в windows с которыми я долго боролся (но победил :))
2. никак не мог сообразить как правильно было сделать запрос аргументов у пользователя построчно
(проблема была в том что я пытался это сделать с sys.args, и даже заполнял этот список аргументов).
Но после полу дня борьбы все таки сделал, и как оказалось это было намного проще чем я сначала городил.

Изначально это было так: https://pastebin.com/L4kSbW18 , и еще куча вариантов, но проблема была в том,
что передавая два пути один за другим, и при этом запуская cmd из папки скрипта в консоли получалась полная каша,
и было просто необходимо добавить построчный запрос по одному пути к файлу за раз.

P.S. Я сделал запрос пути только к двум файлам, а третий по дефолту в папке скрипта находится.
На самом деле они все там лежат, но ничто не мешает раскидать их по разным папкам, я проверял - все работает. 
"""

