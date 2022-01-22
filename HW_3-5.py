"""5. Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:

>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?"""


import random


def get_jokes(a, b, c, n_jokes, repeats=False):
    a, b, c = a.copy(), b.copy(), c.copy()

    list_of_jokes = []

    if n_jokes > 5 and repeats is False:
        print('Кол-во шуток не может быть более 5 при параметре repeats=False')

    elif repeats:

        for i in range(n_jokes):
            sample = (f'{random.choice(a)} '
                      f'{random.choice(b)} '
                      f'{random.choice(c)}')

            list_of_jokes.append(sample)

        return list_of_jokes

    else:
        for i in range(n_jokes):
            sample = (f'{a.pop(random.randrange(len(a)))} '
                      f'{b.pop(random.randrange(len(b)))} '
                      f'{c.pop(random.randrange(len(c)))}')

            list_of_jokes.append(sample)

        return list_of_jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(nouns, adverbs, adjectives, 3))
print(get_jokes(nouns, adverbs, adjectives, 3))

