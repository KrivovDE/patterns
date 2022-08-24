from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size (Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# При возникновении необходимости фильтрации товаров по цвету и размеруб
# можно сделaть так


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    # А потом расширить метод фильтрацией по размеру
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p
# это прямое нарушение ОСР, функциональность должна добавляться
# через расширение, а не через модификацию

