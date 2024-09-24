import threading
import random
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            a = random.randint(50, 500)
            with self.lock:
                self.balance += a
                print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            a = random.randint(50, 500)
            print(f'Запрос на {a}')
            with self.lock:
                if a <= self.balance:
                    self.balance -= a
                    print(f'Снятие: {a}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')