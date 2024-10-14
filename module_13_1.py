import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        delay = 1 / power
        time.sleep(delay)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 0.5))
    task2 = asyncio.create_task(start_strongman('Denis', 2))
    task3 = asyncio.create_task(start_strongman('Apollon', 4))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())