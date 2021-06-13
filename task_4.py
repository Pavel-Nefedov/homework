
class Car: # созадём класс
    def __init__(self, speed, color, name, is_police,): # атрибуты класса
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def car_go():
        print('Поiхали')

    @staticmethod
    def car_slop():
        print('Фсё приехали')

    @staticmethod
    def turn_car(turn):
        if turn == 'прямо':
            print('Едем прямо')
        else:
            print(f'Поворачиваем на{turn}')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        print(f'Вы двигаетесь на {self.name} {self.color} цвета')
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости.')

class Sport_car(Car):
    def show_speed(self):
        print(f'Вы двигаетесь на {self.name} {self.color} цвета')
        super().show_speed()
        if self.speed < 100:
            print('Ты что на тележке в магазине? Почему так медленно')

class Work_car(Car):
    def show_speed(self):
        print(f'Вы двигаетесь на {self.name} {self.color} цвета')
        super().show_speed()
        if self.speed > 50:
            print('Превышение скорости.')

town_car = TownCar(60, 'зелёного', 'калине', True)
town_car.car_go()
town_car.show_speed()
town_car.turn_car('право')

print('\n')

sport_car = Sport_car(99, ',белого', 'жигулях', True)
sport_car.car_go()
sport_car.show_speed()
sport_car.turn_car('прямо')

print('\n')

work_car = Work_car(40, ',ржавого', 'газелька', False)
work_car.car_go()
work_car.show_speed()
work_car.turn_car('налево')
