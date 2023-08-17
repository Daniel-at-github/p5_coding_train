"""
Menger sponge
"""
import proceso

p5 = proceso.Sketch()

# A screen reader accessible description for the canvas.
p5.describe("Menger sponge")

# Variables globales
a = 0
sponge = []


class Box:
    def __init__(self, x, y, z, r):
        self.pos = p5.Vector(x, y, z)
        self.r = r

    def generate(self):
        boxes = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    sum = abs(x) + abs(y) + abs(z)
                    new_r = self.r / 3
                    if sum > 1:
                        b = Box(
                            self.pos.x + x * new_r,
                            self.pos.y + y * new_r,
                            self.pos.z + z * new_r,
                            new_r,
                        )
                        boxes.append(b)
        return boxes

    def show(self):
        p5.push()
        p5.translate(self.pos.x, self.pos.y, self.pos.z)
        # stroke(255);
        # noStroke();
        # noFill();
        # fill(255);
        p5.box(self.r)
        p5.pop()


def setup():
    p5.size(400, 400, p5.WEBGL)
    # A partir de p5.js 0.6.0, el material normal ya no es el predeterminado y
    # debe ser seleccionado explícitamente.
    # p5.ambient_material() # Pero en proceso 0.0.12 aún no está incluido

    # Una lista de objetos Box
    # Comenzar con uno
    b = Box(0, 0, 0, 200)
    sponge.append(b)


def mouse_pressed():
    # Generar el siguiente conjunto de cajas
    global sponge
    next_boxes = [box.generate() for box in sponge]
    sponge = sum(next_boxes, []) # Aplanar lista


def draw():
    global a
    p5.background(51)
    p5.rotate_x(a)
    p5.rotate_y(a * 0.4)
    p5.rotate_z(a * 0.1)
    # ¡Muestra lo que tienes!
    for i in range(len(sponge)):
        sponge[i].show()
    a += 0.01


p5.run_sketch(setup=setup, draw=draw, mouse_pressed=mouse_pressed)
