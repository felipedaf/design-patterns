"""
Strategy Design Pattern

Motivation:
 - Many algorithms can be decomposed into higher-and lower-lever parts

 - Making tea can be decomposed into
    . The process of making a hot beverage(boil water, pour into cup); and
    . Tea-specific things (put teabag into water)

 - The high-level algorithm can then be reused for making coffee or hot chocolate
    . Supported by beverage-specific strategies
"""

from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:

    strategies = {
        OutputFormat.MARKDOWN: MarkdownListStrategy,
        OutputFormat.HTML: HtmlListStrategy
    }

    def __init__(self, list_strategy=HtmlListStrategy()) -> None:
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format):
        self.list_strategy = self.strategies[format]()

    def clear(self):
        self.buffer.clear()

    def __str__(self) -> str:
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)
