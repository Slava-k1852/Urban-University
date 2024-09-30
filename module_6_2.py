
class Vehicle:  # создаём класс Vehicle

    def __init__(self, owner, __model, __color, __engine_power):  # задаём функцию классу Vehicle
        self.owner = owner  # атрибут owner - владелец транспорта. (владелец может меняться)
        self.__model = __model  # атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power  # атрибут __engine_power(int) - мощность двигателя.
        # (мы не можем менять мощность двигателя)
        self.__color = __color  # атрибут __color(str) - название цвета.
        # (мы не можем менять цвет автомобиля своими руками)

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Атрибут класса __COLOR_VARIANTS,
    # в который записан список допустимых цветов для окрашивания.

    def  get_model(self):  # метод get_model - возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self.__model}'
    def get_horsepower(self):  # метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):  # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет: {self.__color}'

    def print_info(self):  # метод print_info - распечатывает результаты методов
        print({self.get_model()}, {self.get_horsepower()}, {self.get_color()})
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):  # метод set_color - принимает аргумент new_color(str),
        # меняет цвет __color на new_color,
        if new_color.lower() in self.__COLOR_VARIANTS:  # если он есть в списке __COLOR_VARIANTS
            self.__color = new_color
        else:  # в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>"
            print(f'Нельзя сменить цвет на: {new_color}')


class Sedan(Vehicle):  # создаём класс Sedan, наследник класса Vehicle

    __PASSENGERS_LIMIT = 5  # атрибут __PASSENGERS_LIMIT = 5
    # (в седан может поместиться только 5 пассажиров)



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
