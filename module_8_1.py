

def add_everything_up(a, b):

    try:
        if type(a) == (int, float) and type(b) == (int, float):
            return a + b

        elif type(a) == str and type(b) == str:
            return a + b

        else:
            raise TypeError

    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
