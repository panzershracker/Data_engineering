# 1. Реализовать вывод информации о промежутке времени
#   в зависимости от его продолжительности duration в секундах:
#   до минуты: <s> сек; до часа: <m> мин <s> сек;
#   до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

def time_by_duration (duration):
    const_minute = 60
    const_hour = const_minute * 60
    const_day = const_hour * 24

    days = duration // const_day
    duration = duration - days * const_day

    hours = duration // const_hour
    duration = duration - hours * const_hour

    minutes = duration // const_minute

    seconds = duration - minutes * const_minute

    print(f'{days} дней {hours} часов {minutes} минут {seconds} секунд \n')

time_by_duration(400153)

# Примечание: подумайте, можно ли использовать цикл для проверки работы кода
# сразу для нескольких значений продолжительности, будет ли тут полезен список?

# Ответ: конечно можно использовать цикл для проверки несколькох значений из списка, пример ниже.

def time_by_duration_from_list (duration_list):
    for i in duration_list:
        print(f'calculating for {i} seconds')
        time_by_duration(i)

time_by_duration_from_list([400153, 4153])

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

# для составления первоначального списка используем генератор:

odd_list = [i**3 for i in range(1, 1001) if i % 2 != 0]

# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#   Например, число «19 ^ 3 = 6859» будем включать в сумму,
#   так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#   Внимание: использовать только арифметические операции!

sum_of_sums = 0

for i in odd_list:
    candidate = sum([int(digit) for digit in str(i)])
    if candidate % 7 == 0:
        sum_of_sums += candidate

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#   сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

odd_list = [i + 17 for i in odd_list]

sum_of_sums_2 = 0

for i in odd_list:
    candidate = sum([int(digit) for digit in str(i)])
    if candidate % 7 == 0:
        sum_of_sums_2 += candidate


# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

n = 100

for i in range(1, n + 1):
    endswith_ = None
    if str(i).endswith('1'):
        endswith_ = ''
    if str(i).endswith(('2', '3', '4')):
        endswith_ = 'а'
    if str(i).endswith(('5', '6', '7', '8', '9', '0')):
        endswith_ = 'ов'
    print(f'{i} процент' + endswith_)



