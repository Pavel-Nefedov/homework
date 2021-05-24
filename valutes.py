import requests

from datetime import date
from decimal import Decimal


def get_currency_rate(currency_code='USD'):
    currency_code = currency_code.upper()

    response_text = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
    currency_index = response_text.find(currency_code)

    if currency_index == -1:
        return

    date_index = response_text.find('Date')

    currency_date = response_text[date_index + 6:date_index + 16]

    day, month, year = (int(x) for x in currency_date.split('.'))
    refined_currency_date = date(year, month, day)

    nominal = get_field('nominal', response_text, currency_index)
    currency_price = \
        get_field('value', response_text, currency_index)

    currency_price = currency_price.replace(',', '.')

    return f'На {refined_currency_date} {nominal} {currency_code} ==' \
        f'{Decimal(currency_price)} Rur'

def get_field(field_name, response_text, currency_index):

    value_start_index = response_text.find(field_name, currency_index) + len(field_name)

    value_end_index = response_text.find('</', value_start_index)
    return response_text[value_start_index:value_end_index]


if __name__ == '__main__':
    from sys import argv
    _module_name, currency_code_arg = argv
    print(get_currency_rate(currency_code_arg))
