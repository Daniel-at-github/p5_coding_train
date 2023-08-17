"""
Snake game
"""
import proceso
import js

p5 = proceso.Sketch()

# A screen reader accessible description for the canvas.
p5.describe("Snake game")


class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def show(self):
        p5.fill(self.color)
        p5.no_stroke()
        p5.square(self.x * square_size, self.y * square_size, square_size)

    def change_color(self, color):
        self.color = color

    def move_to_random_location(self):
        self.x = int(p5.random(0, p5.width // square_size))
        self.y = int(p5.random(0, p5.height // square_size))

    def collision(self, square):
        return self.x == square.x and self.y == square.y

    def __str__(self):
        return f"M({self.x},{self.y})"


class Fruit(Square):
    def __init__(self):
        Square.__init__(self, 0, 0, "green")
        self.move_to_random_location()

    def is_eaten(self, square):
        if self.collision(square):
            self.move_to_random_location()
            return True
        return False


class Snake:
    def __init__(self):
        head = Square(0, 0, "pink")
        head.move_to_random_location()
        self.body = [head]
        self.trail = [Square(-1, -1, "pink") for _ in range(5)]
        self.direction = {"x": 0, "y": 0}
        self.has_eaten = False

    def update(self):
        head = self.body[0]
        x = head.x + self.direction["x"]
        y = head.y + self.direction["y"]
        if (0 <= x < p5.width // square_size) and (
            0 <= y < p5.height // square_size
        ):
            new_head = Square(
                head.x + self.direction["x"],
                head.y + self.direction["y"],
                head.color,
            )
            if any([new_head.collision(body_part) for body_part in self.body]):
                js.console.log(f"💥 Dead ☠️ {new_head}")
                self.log()
                for body_part in self.body:
                    body_part.change_color(board_color)
                    body_part.show()
                self.__init__()

            self.body.insert(0, new_head)
            if not self.has_eaten:
                self.trail = self.body.pop()
                self.trail.change_color(board_color)
            self.has_eaten = False

    def show(self):
        for square in self.body:
            square.show()
        if self.trail:
            self.trail.show()
            self.trail = []

    def eat(self, fruit):
        mouth = self.body[0]
        if fruit.is_eaten(mouth):
            self.has_eaten = True

    def move(self, x, y):
        self.direction["x"], self.direction["y"] = x, y

    def log(self):
        js.console.log(f"🐍{[str(body_part) for body_part in self.body]}")


# Variables globales
square_size = 10
board_color = "gray"
fruit = None
snake = None


def setup():
    global fruit
    global snake

    p5.create_canvas(400, 400)
    p5.frame_rate(10)  # Reducir velocidad
    p5.background(board_color)
    fruit = Fruit()
    snake = Snake()


def draw():
    global fruit
    global snake
    snake.update()
    snake.eat(fruit)
    fruit.show()
    snake.show()


def key_pressed():
    global snake
    if p5.key_code == p5.UP_ARROW:
        snake.move(0, -1)
    elif p5.key_code == p5.DOWN_ARROW:
        snake.move(0, 1)
    elif p5.key_code == p5.LEFT_ARROW:
        snake.move(-1, 0)
    elif p5.key_code == p5.RIGHT_ARROW:
        snake.move(1, 0)


p5.run_sketch(setup=setup, draw=draw, key_pressed=key_pressed)
