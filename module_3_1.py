calls = 0  # переменная (calls = 0) вне функций


def count_calls():  # функция (count_calls), изменяемое в ней значение переменной (calls)
    global calls
    calls += 1  # переменная (calls = calls + 1)


def string_info(string):  # функция (string_info) принимает аргумент - строку
    count_calls()
    return len(string), string.upper(), string.lower()  # возвращает кортеж из: длины этой строки


def is_contains(string, list_to_search):  # функция (is_contains) принимает два аргумента: строку и список
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]  # возвращает (True), если строка в этом списке,
    # (False) - если отсутствует


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
