class Clothes:
    def __init__(self, coat, costume):
        self.coat = coat #пальто
        self.costume = costume #костюм

    def for_coat(self):
        cloath = self.coat / 6.5 + 0.5
        return cloath

    def for_costume(self):
        cloath = 2 * (self.costume / 100) + 0.3
        return cloath

    @property
    def sum_size(self):
        sum = (self.coat / 6.5 + 0.6) + (self.costume / 100 * 2 + 0.3)
        # с помощью super() не вышло вызвать значения, потому и написал их вновь. недочёт
        return sum

clothes = Clothes(48, 180) # первое на пальто, второе на костюм
print(round(clothes.for_coat(), 1), 'кв.м. ткани для пальто')
print(round(clothes.for_costume(), 1), 'кв.м. ткани для костюма')
print(round(clothes.sum_size, 1), 'кв.м. ткани в общем')
