"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта,
а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import itertools
import json
import sys

with open('users.csv', encoding='utf-8') as users, \
        open('hobby.csv', encoding='utf-8') as hobby:

    users_len = sum(1 for i in open('users.csv', encoding='utf-8'))
    hobby_len = sum(1 for i in open('hobby.csv', encoding='utf-8'))

    if users_len >= hobby_len:
        result = {k.rstrip().replace(',', ' '): v.rstrip() for k, v in
                  itertools.zip_longest(users, hobby, fillvalue='None')}

    else:
        sys.exit(1)


print(result)
# out: {
#       'Иванов Иван Иванович': 'скалолазание,охота',
#       'Петров Петр Петрович': 'горные лыжи',
#       'Федоров  Федор  Федорович': 'None'
#       }

with open('user_hobbies.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False)






