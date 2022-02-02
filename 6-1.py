"""
1. Не используя библиотеки для парсинга,
распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

connections = []

with open('nginx_logs.txt', 'r') as file:

    for line in file:

        line = line.split('-')
        ip = line[0]

        line = line[2].split('"')
        line = line[1].split(' ')
        method, path = line[0], line[1]

        connections.append(tuple([ip, method, path]))

for i in connections[:10]:
    print(i)

#out:
# ('93.180.71.3 ', 'GET', '/downloads/product_1')
# ('93.180.71.3 ', 'GET', '/downloads/product_1')
# ('80.91.33.133 ', 'GET', '/downloads/product_1')
# ('217.168.17.5 ', 'GET', '/downloads/product_1')
# ('217.168.17.5 ', 'GET', '/downloads/product_2')
# ('93.180.71.3 ', 'GET', '/downloads/product_1')
# ('217.168.17.5 ', 'GET', '/downloads/product_2')
# ('217.168.17.5 ', 'GET', '/downloads/product_1')
# ('80.91.33.133 ', 'GET', '/downloads/product_1')
# ('93.180.71.3 ', 'GET', '/downloads/product_1')



