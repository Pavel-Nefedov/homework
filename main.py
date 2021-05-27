from utils import currency_rates


for num in currency_rates():
    print(currency_rates(input('Введите название курса валюты: ')))