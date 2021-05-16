number_list = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'fife': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
    }

while True:
    print('Для остановки программы введите "Stop"')
    user_number = input('Введите число от 1 до 10 на английском языке прописью: ')

    if user_number == 'Stop' or user_number == 'stop':
        print('Закругляемся')
        break

    def num_translate(num):
        for key, val in num.items():
            if key == user_number:
                print(val)

    num_translate(number_list)

