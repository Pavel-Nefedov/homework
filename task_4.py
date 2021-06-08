def val_checker(verbosity):
    def _val_checker(func):
        def wrapper(*args):

            if verbosity(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'Ошибка в: "{args}" нужно ввести целое число')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


user_number = int(input('Введите целое число: '))
print(calc_cube(user_number))