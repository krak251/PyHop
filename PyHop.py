import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
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
        try:
            self.background = arcade.load_texture("background.png")
        except FileNotFoundError:
            print("Ошибка: Файл background.png не найден. Убедись, что он в папке с кодом.")
            self.background = None

        # try:
        #     self.hopper_texture = arcade.load_texture("hopper.png")
        # except FileNotFoundError:
        #     print("Ошибка: Файл hopper.png не найден. Убедись, что он в папке с кодом.")
        #     self.hopper_texture = None

        self.platforms = []
        self.score = 0

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background, arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))


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