# Нарушается принцип OCP

class Person:
    def __init__(self):
        # адрес
        self.street_address = None
        self.postcode = None
        self.city = None
        # информация о работе
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'

# Чтобы избавится от такой большой инициализации, необходио применить паттерн СТРОИТЕЛЬ


class PersonBuilder:  # Фасад
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person

# Определяем дочерних строителей - PersonJobBuilder и PersonAddressBuilder


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()
p = pb\
    .lives\
        .at('39 Volodarskogo')\
        .in_city('Voronezch')\
        .with_postcode('396002')\
    .works\
        .at('Police')\
        .as_a('Patrol')\
        .earning(85000)\
    .build()
print(p)
person2 = PersonBuilder().build()
print(person2)