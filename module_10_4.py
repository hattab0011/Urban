import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        expectation = random.randint(3,10)
        time.sleep(expectation)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queve = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.get_free_table()
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел за стол номер {free_table.number}")
            else:
                self.queve.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queve.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if table.guest is None and not self.queve.empty():
                    next_guest = self.queve.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)

    def get_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None


tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()



