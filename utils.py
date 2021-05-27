from datetime import date
from decimal import Decimal
import requests


def currency_rates(CharCode='EUR'):
    CharCode = CharCode.upper()

    response_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_starts_at_index = response_text.find(CharCode)

    if currency_starts_at_index == -1:
        return

    date_index = response_text.find('Date')

    curency_date = response_text[date_index + 6:date_index + 16]

    day, month, year = (int(x) for x in curency_date.split('.'))
    refined_currency_date = date(year, month, day)

    nominal = get_field('<Nominal>', response_text, currency_starts_at_index)
    currency_price = \
        get_field('<Value>', response_text, currency_starts_at_index)
    currency_price = currency_price.replace(',', '.')

    return f'На {refined_currency_date} {nominal} {CharCode}==' \
           f'{Decimal(currency_price)} рубля(ей)'


def get_field(field_name, response_text, currency_starts_at_index):
    value_start_index = response_text.find(
        field_name, currency_starts_at_index
    ) + len(field_name)

    value_end_index = response_text.find('</', value_start_index)

    return response_text[value_start_index: value_end_index]


if __name__ == '__main__':
    from sys import argv

    _module_name, currency_code_arg = argv
    print(currency_rates(currency_code_arg))