import random
# такое решение с матрицей нашел на ютубчике)
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def Mat():
        # сюда введи параметры матрицы
        m = int(input('Столбцов в матрице: ')) # столбцы
        n = int(input('Строк в матрице: ')) # строки
# хотел конечно получить каждое число в матрице рандомным но не смог, сделал так
        a = [[random.randint(0,100)]*m for i in range (n)]
        for i in a:
            print(i)

matrix = Matrix
matrix_print = matrix.Mat()


