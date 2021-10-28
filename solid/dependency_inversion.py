# DIP
# Avoid internal dependency between classes

from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2]


"""
Wrong way to do it

class Research:
    def __init__(self, relationships):
        for r in relationships.relations: # <--- Internal dependency
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John is father of {r[2].name}")
"""

# Right way to do it


class Research:
    def __init__(self, relationships):
        for child in relationships.find_all_children_of("John"):
            print(f'John is father of {child.name}')


if __name__ == "__main__":
    parent = Person("John")
    child1 = Person("Pedro")
    child2 = Person("Francisco")

    relationship = Relationships()
    relationship.add_parent_and_child(parent, child1)
    relationship.add_parent_and_child(parent, child2)

    research = Research(relationship)
