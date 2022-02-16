"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyErr(Exception):
    pass


divider = input('Введите делитель: ')

try:
    if int(divider) == 0:
        raise MyErr('Делитель не должен быть нулем!')

    result = 100 / int(divider)

except (ValueError, MyErr) as e:
    print(e)

else:
    print(f'Result = {result}')