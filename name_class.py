tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '10Б', '9А'
]
"""
(Для себя), yield возвращает значения из функции как и return
"""
def generate():

    for index in range(len(tutors)):
        if index < len(klasses):
            yield tutors[index], klasses[index]#функция возвращает в виде ключ: значение
        else:
            yield tutors[index], None


generate = generate()
print(*generate)

