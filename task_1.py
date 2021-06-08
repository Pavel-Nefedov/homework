import re

email_adress = ['someone@geekbrains.ru']

def email_parse(url):
    RE_EMAIL = re.compile(r'\w+[a-z]\@\w+[a-z].\w+[.*\b]')
    for error in url:
        assert RE_EMAIL.match(error), f'ошибка в {error}'
    else:
        RE_GET_PARSER = re.compile(r'(?P<username>\w+)@(?P<domain>\w+(.*\b))')
        print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(*url)), sep=', ')

email_parse(email_adress)
