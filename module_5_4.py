class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if len(args) == 0:
            cls.houses_history.append(kwargs['name'])
            instance.name = kwargs['name']
            instance.number_of_floors = kwargs['number_of_floors']
        else:
            cls.houses_history.append(args[0])
            instance.name = args[0]
            instance.number_of_floors = args[1]
        return instance


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if new_floor <=0 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            print(new_floor)


    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


    def __add__(self, other):
        return House(self.name, self.number_of_floors + other)


    def __radd__(self, other):
        return self.__add__(other)


    def __iadd__(self, other):
        self.number_of_floors += other
        return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)