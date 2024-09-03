def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])


values_list = [False, [5, 7, 9], 'Slava']
values_dict = {'a': 34, 'b': 88, 'c': 163}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
