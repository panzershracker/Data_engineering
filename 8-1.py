"""
1. Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:

>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""


import re


def email_parse(email_address):

    template = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email_dict = {}

    if template.match(email_address):

        email_dict['username'], email_dict['domain'] = email_address.split('@')[0], \
                                                       email_address.split('@')[1].split('.')[0]

        return email_dict

    else:
        raise ValueError(f'Неверный email')


print(email_parse('student@geekbrains.ru'))
# out: {'username': 'student', 'domain': 'geekbrains'}

"""
re.compile() имеет смысл использовать, если будет обрабатываться большое кол-во адресов.
В ином случае - не обязательно.
"""


