import os

file_statistic = {'10': 0, '100': 0, '1000': 0, '10000': 0, '100000': 0, 'Директория': 0, 'Файл': 0}

#добавляю по размеру файлов
def file_size(file_to_size):
    file_statistic['Файл'] += 1
    if 0 <= os.path.getsize(file_to_size) <= 10:
        file_statistic['10'] += 1
    elif 10 < os.path.getsize(file_to_size) <= 100:
        file_statistic['100'] += 1
    elif 100 < os.path.getsize(file_to_size) <= 1000:
        file_statistic['1000'] += 1
    elif 1000 < os.path.getsize(file_to_size) <= 10000:
        file_statistic['10000'] += 1
    elif 10000 < os.path.getsize(file_to_size) <= 100000:
        file_statistic['100000'] += 1


def file_or_not(file_name, file_directory):
    if os.path.isfile(f'{file_directory}/{file_name}'):#если путь path существует
        file_size(f'{file_directory}/{file_name}')
    else:
        file_statistic['Директория'] += 1#если paht = false

#функция для вывода
def main():
    file_dir = input('Введите путь к директории для вывода статистики по размерам файлов: ')
    try:
        for file in os.listdir(file_dir):
            file_or_not(file, file_dir)
    except FileNotFoundError:
        print('Ошибка\nТакого пути не существует')
    print(file_statistic)


print(main())

#if __name__ == '__main__':
# main()

