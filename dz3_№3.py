from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

number_fun = int(input('Введите количество шуток: '))

def get_jokes(joke):
    """
    Данный код рассчитан на вывод 5 результатов без повторений
    так как .remove() удаляется из списка каждый выведенный результат
    ниже есть вариант для бесконечного количества выводов
    """
    ready_jokes = [] #готовый список для вывода
    i = 1 #счетчик

    while i <= joke:
        if joke > 5:
            print('дальше не работаем')
            break

        random_idx = randrange(len(nouns))
        one_word = nouns[random_idx]
        nouns.remove(one_word)
        random_idx = randrange(len(adverbs))
        two_word = adverbs[random_idx]
        adverbs.remove(two_word)
        random_idx = randrange(len(adjectives))
        three_word = adjectives[random_idx]
        adjectives.remove(three_word)

        ready_joke = (one_word, two_word, three_word)
        ready_jokes.append(' '.join(ready_joke))
        i += 1
    return ready_jokes


    # while i <= joke:
    #
    #     random_idx = randrange(len(nouns))
    #     one_word = nouns[random_idx]
    #     random_idx = randrange(len(adverbs))
    #     two_word = adverbs[random_idx]
    #     random_idx = randrange(len(adjectives))
    #     three_word = adjectives[random_idx]
    #
    #     ready_joke = (one_word, two_word, three_word)
    #     ready_jokes.append(' '.join(ready_joke))
    #     i += 1
    # return ready_jokes

print(get_jokes(number_fun))
