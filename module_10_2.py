from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.enemies > 0:
            sleep(1)
            self.days += 1
            self.enemies -= self.power
            enemies_left = max(self.enemies, 0)
            print(f'{self.name}, сражается {self.days} день(дня)..., осталось {enemies_left} воинов')

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")