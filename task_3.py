class Cell:
    def __init__(self, cell):
        self.number_cell = cell

    def __add__(self, other):  # сложение
        return f'{"сложение равно"} {self.number_cell + other.number_cell}'

    def __sub__(self, other):  # вычитание
        subtraction_cell = self.number_cell - other.number_cell
        if subtraction_cell > 0:
            return f'{"разность равна"} {subtraction_cell}'
        else:
            return "Вычитание невозможно"

    def __mul__(self, other):  # умножение
        return f'{"умножение равно"} {self.number_cell * other.number_cell}'

    def __floordiv__(self, other):  # деление без остатка
        return f'{"деление без остатка равно"} {self.number_cell // other.number_cell}'

    def make_order(self, cell_row):
        list_cells_print = []
        division_without_remainder = self.number_cell // cell_row  # деление без остатка
        remainder_of_the_division = self.number_cell % cell_row  # остаток от деления

        if remainder_of_the_division > 0: # если остаток от деления больше нуля
            for i in range(division_without_remainder):
                add_in_list = "*" * cell_row + "\n"
                list_cells_print.append(add_in_list) # добавляет основные ряды клеток

            add_in_list = "*" * remainder_of_the_division    # а тут высчитаем клетки, если их не хватает на полный ряд
            list_cells_print.append(add_in_list)

        elif remainder_of_the_division == 0: # если остаток от деления равен нулю
            for i in range(division_without_remainder):
                add_in_list = "*" * cell_row + "\n"
                list_cells_print.append(add_in_list) # добавляет оставшиеся клетки
        return list_cells_print

user_cells_row = int(input('Введите кол-во ячеек в ряду: '))
cell_1 = Cell(int(input('Введите кол-во ячеек в первой клетке: ')))
cell_2 = Cell(int(input('Введите кол-во ячеек во второй клетке: ')))

print(cell_1 + cell_2) # ставим знак который нужен + - * //
print("Ряды ячеек во второй клетке: ", "\n", * cell_2.make_order(user_cells_row), sep='') # задаём количество ячеек в ряду
