# - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
# - Выведите на экран словарь my_dict.
# - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
# - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
# - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
# - Выведите на экран словарь my_dict.
# - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
# - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
# - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
# - Удалите один любой элемент из множества my_set.
# - Выведите на экран измененное множество my_set.
my_dict = {'Andrey' : 1990, 'Max' : 1991, 'Oleg' : 1992}
print(my_dict)
print(my_dict.get('Andrey'))
print(my_dict.get('Klim'))
my_dict.update({'Olya' : 1993,
                'Gena' : 1994})
M = my_dict.pop('Max')
print(M)
print(my_dict)
my_set = {1, 2, 1, 2, 'Str', 12.1, 12.1}
print(my_set)
my_set.update({3,6})
my_set.discard(1)
print(my_set)

