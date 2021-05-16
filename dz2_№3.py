def thesaurus(name):
    """
    .satdefault - передаю первую букву имени и создаю список
    в который потом с помощью .append добавляю имя по ключу (первой букве)
    результат никуда не возвращаю и не записываю, он через name1=... уже в словаре.
    """
    d1 = dict()

    for key in name:
        first_letter = key[0]
        name1 = d1.setdefault(first_letter, [])
        name1.append(key)
    return d1

names = "Иван", "Мария", "Петр", "Илья", "Анна", "Ярик", "Дима"
print(thesaurus(names))

