from DrawingAPI1 import DrawingAPI1
from DrawingAPI2 import DrawingAPI2
from DrawingAPI3 import DrawingAPI3
from CircleShape import CircleShape

class BridgePattern(object):
    @staticmethod
    def test():
        shapes = [
            CircleShape(1.0, 2.0, 3.0, DrawingAPI1()),
            CircleShape(5.0, 7.0, 11.0, DrawingAPI2()),
            CircleShape(6.0, 6.0, 10.0, DrawingAPI3())

        ]

        for shape in shapes:
            shape.resize_by_percentage(2.5)
            print(shape.draw())


BridgePattern.test()
