import time

color_red = 7
color_yellow = 2  # время таймера для светофора
color_green = 3


class TrafficLight: # TrafficLight - класс

    def __init__(self):
        self.__color = None


    def running(self):
        color = "Сигнал светофора - 'Красный'"
        print(color, ". Оставшееся время сек:")
        for time_sec in range(color_red, 0, - 1):  # отсчет времени через цикл
            time.sleep(1)   # интервал отсчета в сек, если убрать то выполняет сразу
            print(f'({time_sec})', end='  ')
        print(f"\n-----------------------")  # чтоб понятно было что делает))

# далее повторение кода выше только с другими переманными цвета

        self.__color = "Сигнал светофора - 'Жёлтый'"
        print(self.__color, ". Оставшееся время сек:")
        for time_sec in range(color_yellow, 0, - 1):
            time.sleep(1)
            print(f'({time_sec})', end=' ')
        print(f"\n-----------------------")

        self.__color = "Сигнал светофора - 'Зеленый'"
        print(self.__color, ". Оставшееся время сек:")
        for time_sec in range(color_green, 0, - 1):
            time.sleep(1)
            print(f'({time_sec})', end=' ')
        print(f"\nГазуй газуй не жалей ее")


traffic_lights = TrafficLight() # создаём экземпляр
traffic_lights.running() # вызываем
