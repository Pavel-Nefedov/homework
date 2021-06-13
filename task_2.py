class Road:

    thickness = 5 # толщина полотна в см
    meter_mass = 25 # масса одного м*2

    def __init__(self, length, width):
        self._length = length # длинна дороги
        self._width = width # ширина дороги
#не обязательно называть self, можно по другому
    def running(self): # перемножаю все значения
        return (
            self._width *
            self._length *
            self.meter_mass *
            (self.thickness / 100) # привожу толщинну в см в метры
        )

if __name__ == '__main__':
    road = Road(250, 10) # передаю длинну и ширину дороги
    print(f'{round(road.running())} тонн') # округляю до целых и вывожу
