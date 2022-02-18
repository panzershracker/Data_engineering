"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
from datetime import datetime


class Date:

    @classmethod
    def extract_date(cls, date):
        date = cls.date_validation(date)

        day, month, year = date.day, date.month, date.year
        return day, month, year

    @staticmethod
    def date_validation(str_date):
        template = '%d-%m-%Y'

        try:
            date = datetime.strptime(str_date, template)
            print('Valid date format')
        except ValueError as e:
            print(f'{e}, \nВведите дату в формате "dd-mm-yyyy"')
        else:
            return date


test_1 = Date()
print(test_1.extract_date('01-02-2022'))



