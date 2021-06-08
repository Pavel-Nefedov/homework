def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')#выводим каждое число и его тип
        result = func(*args)#обращаюсь к декоратору(если правильно понял :) )
        return result
    return wrapper

@type_logger#это называется "замаскировать работу декоратора"?
def sum_number(x, y):
    return f'{x * y} отдельная строка'

print(sum_number(8,5))

#По заданию нужно вывести тип значения функции
print(sum_number)#это он?


