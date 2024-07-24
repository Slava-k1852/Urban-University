grades = [[4, 3, 5, 4, 5], [3, 4, 2, 3], [5, 5, 2, 3, 4], [4, 4, 3, 4], [5, 3, 5, 4, 5]]  # 5-ть списков в списке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # словарь с 5-ю ключами
grades_s = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]),
            sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
            sum(grades[4]) / len(grades[4])]  # sum сумма балов по индексу ([0] - [4, 3, 5, 4, 5]) делим на колличество
#           баллов (len - [4, 3, 5, 4, 5]), / 5 = 4.2, и так с каждым списком с помошью ииндекса [0] - [4]
students_sort = sorted(students)  # sorted сортирует данные в алфавитном или в арифметическом порядке
dict_ = dict(zip(students_sort, grades_s))  # команда zip создаёт словарь,
#                                             соединяя ключ (students_sort) со значением (grades_s)
print(dict_)
