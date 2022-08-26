from abc import abstractmethod, ABC


# Создание интерфейсов содержащих много програмных членов - не лучшая идея


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# пример плохого кода. MultiFunctionPrinter наследуясь от Machine, требует всех его методов,


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

# а вот OldFashionedPrinter требует только один метод от Machine, это плохо


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


# Пример возможной реализации аналогичного функционала с учетом ISP

# Создаем три класса, по одному для каждого нужного метожа
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


# При создании нужного объекта просто наследуемся от тех класссов, у которых подхлдящие методы
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass

