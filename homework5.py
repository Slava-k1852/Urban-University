immutable_var = (7, 12, 45, 'f', 'e', 'y', False)  # immutable_var переменная, ей присвоен кортеж
# immutable_var[2] = 50  # TypeError: 'tuple' object does not support item assignment
# immutable_var[6] = 'm'  # кортеж – это неизменяемая упорядоченная коллекция
print('Immutable tuple:', immutable_var)
mutable_list = [10, 19, 64, False, 'Hello']  # mutable_list переменная, ей присвоен список из 3х разных типов
mutable_list[0] = 100  # integer меняем 10 на 100
mutable_list[4] = 'Goodbye'  # string меняем Hello на Goodbye
mutable_list[3] = True  # boolean меняем False на True
mutable_list.append('Modified')  # .append добавляем объект в конец списка
print('Mutable list:', mutable_list,)
