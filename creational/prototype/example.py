"""
Prototype Design Pattern

Motivation:
 - Complicated objects (e.g. cars) aren't designed from scratch
 - An existing (partially or fully constructed) design is a Prototype
 - We make a copy (clone) the prototype and customize it
 - We make the cloning convenient (via a Factory)
"""

import copy

class Address:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self) -> str:
        return f'{self.city} - {self.street_address} - {self.country}'


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'


john = Person('John', Address('123 Londoon Road', 'London', 'UK'))
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '321 London Road'
print(john)
print(jane)
