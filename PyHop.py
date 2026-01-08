import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PyHop"
GRAVITY = 0.98
JUMP_SPEED = 12
COLORS = [
    arcade.color.WHITE,
    arcade.color.BLACK,
    arcade.color.ORANGE,
    arcade.color.RED,
]


class PyHop(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # текстурки
        self.background = arcade.load_texture("background.png")
        # self.hopper = arcade.load_texture("hopper.png")
        self.platforms = []
        self.score = 0

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def update(self, delta_time):
        pass

    def create_platform(self):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.A:
            pass
        elif symbol == arcade.key.D:
            pass

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A:
            pass
        elif symbol == arcade.key.D:
            pass

if __name__ == "__main__":
    game = PyHop(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()