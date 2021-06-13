class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return f"{self.position}, {self.name} {self.surname}"
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

call_position = Position("Pavel","Nefedov","developera",{"wage": 4000, "bonus": 16000})

print(f"По поводу оплаты труда Junior {call_position.get_full_name()} - сначала зп будет "
      f"{call_position.get_total_income()}, потом {call_position.get_total_income()*5}")
print('Хорошо, приду потом :D')