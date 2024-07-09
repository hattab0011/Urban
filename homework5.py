# - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# - Выполните операции вывода кортежа immutable_var на экран.
# - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# - Измените элементы списка mutable_list.
# - Выведите на экран измененный список mutable_list.
immutable_var = ('1', 2, True)
print(immutable_var)
immutable_var[0] = '2'
mutable_list = [1, 2, True]
mutable_list[2] = False
print(mutable_list)