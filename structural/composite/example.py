"""
Composite Design Pattern

Motivation:
 - Objects use other objects properties/members through inheritance and composition
 - Composition lets us make compound objects
 - Composite design pattern is used to treat both single(scalar) and 
 composite objects uniformly
"""


class GraphicObject:
    def __init__(self, color=None) -> None:
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'

if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Square('Yellow'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)