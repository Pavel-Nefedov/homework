class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        return "Запуск отрисовки"

class Pen(Stationery):
    @staticmethod
    def draw():
        return "Ручку"

class Pencil(Stationery):
    @staticmethod
    def draw():
        return "Карандаш"

class Handle(Stationery):
    @staticmethod
    def draw():
        return "Маркер"


start_draw = Stationery

writing = Pen, Pencil, Handle# список классов для вывода

for i in writing:
    pen = i
    print(f'{start_draw.draw()} в руки взяли {pen.draw()} начинаем рисовать')