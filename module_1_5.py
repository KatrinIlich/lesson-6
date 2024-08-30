#Создание кортежа и присвоение разных типов данных
immutable_var = ("hello", True, 10,  2)
#Вывод на экран
print("Immutable tuple:", immutable_var)
#Изменение кортежа
#immutable_var[2]=13
#Кортеж не поддерживает изменение и обращение по элементам
#Создание списка по элементам
mutable_list = [1, 2, 3, 4]
mutable_list[0] = "Hi"
mutable_list[3] = True
print("Mutable list:", mutable_list)