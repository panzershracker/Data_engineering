"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов;
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

import time
from collections import Counter


connections = []

with open('nginx_logs.txt', 'r') as file:
    n_rows = 0

    for line in file:

        line = line.split('-')
        ip = line[0]

        line = line[2].split('"')
        line = line[1].split(' ')
        method, path = line[0], line[1]

        connections.append(tuple([ip, method, path]))
        n_rows += 1

start_time = time.perf_counter()

ip_counts = Counter(i[0] for i in connections)
spammer = ip_counts.most_common(1)

print(spammer)
# out: [('216.46.173.126 ', 2350)]

print(f'Время на выполнение скрипта с "counter" {time.perf_counter() - start_time}\n\n')
# out: Время на выполнение скрипта с "counter" 0.022328299935907125
# ================================================================================

start_time_2 = time.perf_counter()

ips = [i[0] for i in connections]

ips_set = set(ips)  # сделаем сет для списка всех ip адресов
# для более быстрого подсчета и снижения сложности операции.

ip_counts_2 = {i: ips.count(i) for i in ips_set}
spammer_2 = dict(sorted(ip_counts_2.items(), key=lambda x: x[1], reverse=True))

print(next(iter(spammer_2.items())))
# out: ('216.46.173.126 ', 2350)

print(f'Время на выполнение скрипта с "count" {time.perf_counter() - start_time_2}')
# out: Время на выполнение скрипта с "count" 4.3638419000199065






