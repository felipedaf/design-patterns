"""
Builder Design Pattern

Motivation:
 - Some objects are simple and can be created in a single initializer call
 - Other objects require a lot of ceremony to create
 - Having an object with 10 initializer arguments is not productive
 - Instead, opt for piecewise construction
 - Builder provides an API for constructing an object step-by-step
"""

from abc import ABC, abstractmethod


class HtmlVisible(ABC):
    @abstractmethod
    def str(self, tab_level):
        pass


class HtmlContent(HtmlVisible):
    def __init__(self, content) -> None:
        self.content = content

    def str(self, tab_level):
        return tab_level * "  " + self.content + "\n"


class HtmlElement(HtmlVisible):
    def __init__(self, tag, id) -> None:
        self.tag = tag
        self.parent = None
        self.children = []
        self.id = id

    def add_child(self, htmlElement):
        htmlElement.parent = self
        self.children.append(htmlElement)

    def add_content(self, content: str):
        self.children.append(content)

    def str(self, tab_level):
        children_reprs = []
        for child in self.children:
            children_reprs.append(child.str(tab_level + 1))

        return tab_level * "  " + f"<{self.tag}>\n" +\
            "".join(children_reprs) +\
            tab_level * "  " + f"</{self.tag}>\n"


class HtmlBuilder:
    def __init__(self, root: HtmlElement = None) -> None:
        self.root: HtmlElement = root
        self.elements_by_ids = dict()
        self.elements_by_ids[root.id] = root

    def add_child(self, element_or_content, parent_id):
        if not parent_id in self.elements_by_ids:
            return

        if isinstance(element_or_content, HtmlElement) and element_or_content.id in self.elements_by_ids:
            return

        parent_element: HtmlElement = self.elements_by_ids[parent_id]

        if isinstance(element_or_content, HtmlElement):
            self.elements_by_ids[element_or_content.id] = element_or_content
            parent_element.add_child(element_or_content)

        else:
            parent_element.add_content(element_or_content)

    def str(self):
        return self.root.str(0)


if __name__ == "__main__":
    li = HtmlElement("li", 1)
    content = HtmlContent("Seila qualquer coisa aqui!")
    li2 = HtmlElement("li", 2)
    content2 = HtmlContent("Qualquer outra coisa aqui!")
    ul = HtmlElement("ul", 3)

    builder = HtmlBuilder(ul)
    builder.add_child(li, 3)
    builder.add_child(li2, 3)
    builder.add_child(content2, 1)
    builder.add_child(content, 2)


    print(builder.str())
