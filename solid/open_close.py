from enum import Enum


class ProductColor(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    ORANGE = 4


class ProductSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product():
    def __init__(self, name: str, color: ProductColor, size: ProductSize) -> None:
        self.name = name
        self.color = color
        self.size = size

    def __str__(self) -> str:
        return f"{self.name} - {self.color} - {self.size}"

    def __repr__(self) -> str:
        return f"{self.name} - {self.color} - {self.size}"


class ProductFilter():
    @staticmethod
    def filter_by_color(products, color: ProductColor):
        for product in products:
            if product.color == color:
                yield product

    @staticmethod
    def filter_by_size(products, size: ProductSize):
        for product in products:
            if product in products:
                if product.size == size:
                    yield product


class ProductFilter2():
    def __init__(self, product_type) -> None:
        self.props = []

        for prop, _ in product_type.__dict__.items():
            if prop[0] == "_" and prop[-1] == "_":
                continue

            self.props.append(prop)

    def filter(self, products, **kwargs):
        filtered_products = []
        for key in kwargs:
            if not key in self.props:
                raise Exception(f"The property {key} doesn't belong to this product")

        for product in products:
            product_props = product.__dict__

            matched_all_filters = True
            for key in kwargs:
                if not key in product_props or product_props[key] != kwargs[key]:
                    matched_all_filters = False
                    break
            if matched_all_filters:
                filtered_products.append(product)

        return filtered_products


if __name__ == "__main__":
    my_products = [
        Product('bola', ProductColor.RED, ProductSize.SMALL),
        Product('brinquedo', ProductColor.BLUE, ProductSize.LARGE),
        Product('comida', ProductColor.RED, ProductSize.MEDIUM)
    ]

    product_filter = ProductFilter2(my_products[0])

    filtered_products = product_filter.filter(
        my_products, color=ProductColor.RED)

    print(filtered_products)
