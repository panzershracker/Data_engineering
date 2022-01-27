"""
1. Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield, например:

>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
"""

def odd_nums(n):

    for i in range(1, n + 1, 2):
        yield i

odd_nums_n = odd_nums(15)

print(*odd_nums_n)
# out: 1 3 5 7 9 11 13 15
