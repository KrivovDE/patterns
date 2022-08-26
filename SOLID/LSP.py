class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

# Добавление такого класса-квадрато-как частного случая наследования, является нарушением LSP


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


# Создаем функцию для использования этого прямоугольника


def use_it(rect):
    w = rect.width
    target_area = rect.area
    rect.height = 10
    expected = int(w * 10)# Проверяем если заданную высоту умножить на 10
    print(f'Проверяемя площадь = {expected} \nЗаданная площадь = {target_area}')


rc = Rectangle(2, 3)
use_it(rc)

# Проверяемя площадь = 20
# Заданная площадь = 6


sq = Square(5)
use_it(sq)

# Проверяемя площадь = 50 --> Ошибка, верно 25
# Заданная площадь = 25

# принцип нарушен, так как не получилось использовать наследника (причина в строк. 51)
