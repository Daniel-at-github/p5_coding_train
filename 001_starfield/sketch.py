"""
Starfield
"""
import random
import proceso

p5 = proceso.Sketch()

# A screen reader accessible description for the canvas.
p5.describe("Starfield")


class Star:
    def __init__(self):
        self.x = p5.random(-p5.width, p5.width)
        self.y = p5.random(-p5.height, p5.height)
        self.z = p5.random(p5.width)
        self.pz = self.z

    def update(self):
        self.z = self.z - speed
        if (
            self.z < 1
            or not (-1 < self.x / self.z < 1)
            or not (-1 < self.y / self.z < 1)
        ):
            self.z = p5.width
            self.x = p5.random(-p5.width, p5.width)
            self.y = p5.random(-p5.height, p5.height)
            self.pz = self.z

    def show(self):
        p5.fill(255)
        p5.no_stroke()

        sx = p5.remap(self.x / self.z, 0, 1, 0, p5.width / 2)
        sy = p5.remap(self.y / self.z, 0, 1, 0, p5.height / 2)

        r = p5.remap(self.z, 0, p5.width, 4, 0)
        p5.ellipse(sx, sy, r, r)

        px = p5.remap(self.x / self.pz, 0, 1, 0, p5.width / 2)
        py = p5.remap(self.y / self.pz, 0, 1, 0, p5.height / 2)

        self.pz = self.z

        p5.stroke(255)
        p5.stroke_weight(r)
        p5.line(px, py, sx, sy)


# Variables globales
speed = 1
stars = []


def setup():
    p5.create_canvas(800, 800)
    p5.background(0)
    for _ in range(200):
        stars.append(Star())


def draw():
    global speed
    speed = p5.remap(p5.mouse_x, 0, p5.width, 0, 50)
    p5.background(0)
    p5.translate(p5.width / 2, p5.height / 2)

    for star in stars:
        star.update()
        star.show()


p5.run_sketch(setup=setup, draw=draw)
