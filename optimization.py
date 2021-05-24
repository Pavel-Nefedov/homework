from time import perf_counter
start = perf_counter()
"""
src.count(element) показывает сколько раз элемент появляется в списке
и если == 1 раз то он уникален 
"""
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

unique_brands = [element for element in src if src.count(element) == 1]

print(unique_brands, perf_counter() - start)
print(type(unique_brands))
#можете подсказать почему здесь каждый раз файл выполняется разное количество времени?
