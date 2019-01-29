from Shape import Shape

class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        super(CircleShape, self).__init__(drawing_api)

    def draw(self):
        return self.drawing_api.draw_circle(
            self.x, self.y, self.radius
        )

    def resize_by_percentage(self, percent):
        self.radius *= (1 + percent/100)
