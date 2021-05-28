# не смог сделать сам, взял у тебя решение. Слишком долго завис на парсинге, на остальное времени не хватило
#Возможно успею доделать до того как ты начнешь проверять)))
import sys


def add_sale(record_to_add):
    with open('bakery.csv', 'a', encoding='utf=8') as file:
        file.write(f'{record_to_add}\n')


if __name__ == '__main__':
    program, price_rec = sys.argv
    add_sale(price_rec)