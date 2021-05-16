while True:
    print('Для остановки программы введите "стоп"')
    user_number = input('Введите число от 1 до 10 на английском языке прописью: ')

    if user_number == 'Стоп' or user_number == 'стоп':
        print('Закругляемся')
        break

    def num_translate(num):
        if num == 'one':
            print('один')
        elif num == 'two':
            print('два')
        elif num == 'three':
            print('три')
        elif num == 'four':
            print('четыре')
        elif num == 'fife':
            print('пять')
        elif num == 'six':
            print('шесть')
        elif num == 'seven':
            print('семь')
        elif num == 'eight':
            print('восемь')
        elif num == 'nine':
            print('девять')
        elif num == 'ten':
            print('десять')
        else:
            print('None')

    num_translate(user_number)
