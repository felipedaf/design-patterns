"""
Proxy Design Pattern

Motivation:
 - Provide a substitute or placeholder for another object.
    A proxy controls access to the original object, allowing you to perform something
    either before or after the request gets through to the original object
"""

# Protection proxy

class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")

class CarProxy:
    def __init__(self, driver) -> None:
        self.driver = driver
        self._car = Car(driver)
    
    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young')

class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Virtual proxy

class Bitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')

class LazyBitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        
        self._bitmap.draw()

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


if __name__ == "__main__":
    driver = Driver('John', 20)
    car = Car(driver)
    car.drive()

    bmp = Bitmap('facepalm.jpg')
    draw_image(bmp)