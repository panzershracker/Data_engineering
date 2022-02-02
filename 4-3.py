"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

import requests
from datetime import datetime

def currency_rates(val):

    val = val.upper()

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/95.0',
               'Accept-Language': 'ru-RU'}

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    with requests.Session() as session:
        session.headers = headers

        response = session.get(url)

        if val not in response.text:
            return None

        else:
            result = []

            date = response.text.split('Date=')
            date = date[1].split(' ')
            date = date[0].split('"')
            date = datetime.strptime(date[1], '%d.%m.%Y')
            result.append(date.date())

            cur = response.text.split(f'{val}')[1:]
            cur = cur[0].split('Value')[1]
            cur = float(cur[1:-2].replace(',', '.'))
            result.append(cur)

        return tuple(result)


print(type(currency_rates('eur')[0]), type(currency_rates('eur')[1]))
# out: <class 'datetime.date'> <class 'float'>

print(currency_rates('eur'))
# out: (datetime.date(2022, 1, 29), 86.6419)

print(currency_rates('usd'))
# out: (datetime.date(2022, 1, 29), 77.8174)
