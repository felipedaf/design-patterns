"""
Facade Design Pattern

Motivation:
 - Balancing complexity and presentation/usability
 - Typical home
    . Many subsystems (electrical, sanitation)
    . Complex internal structure
    . End user is not exposed to internals

 - Same with software!
    . Many systems working to provide flexibility
    . API consumers want it to "just work"
"""

class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width*height)


    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text

class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index+self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        self.current_viewport.get_char_at(index)