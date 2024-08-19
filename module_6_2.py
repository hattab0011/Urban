class Vehicle:
    def __init__(self, _model: str, owner: str, _engine_power: int, _color: str):
        self._model = _model
        self.owner = owner
        self._engine_power = _engine_power
        self._color = _color

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']


    def get_model(self):
        return f"Модель: {self._model}"


    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power}"


    def get_color(self):
        return f"Цвет: {self._color}"


    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(self.owner)

    def set_color(self, new_color):
        if new_color.lower() in  self.__COLOR_VARIANTS:
            self._color = new_color
            print(f"Новый цвет: {new_color}")
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Toyota Mark II', 'Fedos', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()