"""
4. * (вместо 3) Решить задачу 3 для ситуации,
когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов — получить отдельно фамилию,
имя и отчество для пользователей и название каждого хобби:
преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
"""


import sys
import json
import itertools

with open('users.csv', encoding='utf-8') as users, \
        open('hobby.csv', encoding='utf-8') as hobby, \
        open('user_hobbies_2.txt', 'w', encoding='utf-8') as file:

    for u_row, h_row in itertools.zip_longest(users, hobby, fillvalue='None'):

        result = f'{u_row.rstrip().replace(",", " ")} : {h_row.rstrip()}\n'
        file.write(result)

# Вроде все сделал, но почему то не получается записать словарь в файл нормально.


