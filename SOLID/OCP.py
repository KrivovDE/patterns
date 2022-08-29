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


#Применен корпоративный шаблон Specification

class Specification:
    """
    Класс проверяет удовлетворяет ли конкретный элимент определенному критерию
    """
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    """
    Фильтер продуктов по цвету
    """
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    """
    Фильтер продуктов по размеру
    """
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

# создаем список продуктов по которым проходимся циклом
products = [apple, tree, house]

# Ищем все зеленые продукты
# фильтр который создан с помощью шаблона спецификации
bf = BetterFilter()
# Создаем спицификакцию
green = ColorSpecification(Color.GREEN)

for p in bf.filter(products, green):
    print(f'{p.name}  - точно зеленый')





