def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            result += i
    except TypeError as exc:
        incorrect_data += 1


    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("В numbers записан некорректный тип данных")

        total, incorrect_data = personal_sum(numbers)

        return total / (len(numbers) - incorrect_data)
    except ZeroDivisionError as exc_2:
        return 0
    except TypeError as exc_3:
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать