import arcade
import random

# Константы
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Doodle Jump Python"

# Параметры игры
GRAVITY = 0.5
JUMP_SPEED = 12
PLATFORM_SPACING = 120  # Расстояние между платформами
PLAYER_MOVEMENT_SPEED = 5


class GameView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Списки спрайтов
        self.player_list = None
        self.platform_list = None

        # Переменные игрока
        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList()
        self.score = 0

        # Создание игрока
        self.player_sprite = arcade.SpriteSolidColor(30, 30, arcade.color.WHITE)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = 150
        self.player_list.append(self.player_sprite)

        self.a = True
        # Начальная генерация платформ
        for y in range(
                100,
                SCREEN_HEIGHT +
                PLATFORM_SPACING,
                PLATFORM_SPACING):
            self.create_platform(y)



    def create_platform(self, y_position):
        if self.a:
            platform = arcade.SpriteSolidColor(
                60,
                10,
                arcade.color.LIGHT_GREEN)
            platform.center_x = SCREEN_WIDTH // 2
            platform.center_y = y_position
            self.platform_list.append(platform)
            self.a = False
            return
        platform = arcade.SpriteSolidColor(
            60,
            10,
            arcade.color.LIGHT_GREEN)
        platform.center_x = SCREEN_WIDTH // 2
        platform.center_y = y_position
        self.platform_list.append(
            platform
        )

    def on_draw(self):
        self.clear()
        self.platform_list.draw()
        self.player_list.draw()

        # Отображение счета
        arcade.draw_text(f"Score: {int(self.score)}",
                         10,
                         SCREEN_HEIGHT -
                         30,
                         arcade.color.WHITE, 16)

    def on_update(self, delta_time):
        # Применяем гравитацию
        self.player_sprite.change_y -= GRAVITY
        self.player_sprite.update()

        # Проверка столкновения с платформой (только при падении)
        if self.player_sprite.change_y < 0:
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.platform_list)
            if hit_list:
                # Прыгаем, если коснулись платформы верхней частью или центром
                self.player_sprite.change_y = JUMP_SPEED

        # Бесконечный экран по горизонтали (как в Doodle Jump)
        if self.player_sprite.left > SCREEN_WIDTH:
            self.player_sprite.right = 0
        elif self.player_sprite.right < 0:
            self.player_sprite.left = SCREEN_WIDTH

        # ПРОЦЕДУРНАЯ ГЕНЕРАЦИЯ И СКРОЛЛИНГ
        # Если игрок выше середины экрана
        if self.player_sprite.center_y > SCREEN_HEIGHT / 2:
            shift = self.player_sprite.center_y - SCREEN_HEIGHT / 2
            self.player_sprite.center_y = SCREEN_HEIGHT / 2

            # Двигаем платформы вниз
            for platform in self.platform_list:
                platform.center_y -= shift

            self.score += shift ** 300

        # Удаляем ушедшие вниз платформы и создаем новые сверху
        for platform in self.platform_list:
            if platform.top < 0:
                platform.remove_from_sprite_lists()

                # Генерируем новую платформу выше самой верхней
                top_y = max([p.center_y for p in self.platform_list])
                self.create_platform(top_y + PLATFORM_SPACING)

        # Проверка падения (Game Over)
        if self.player_sprite.top < 0:
            self.setup()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player_sprite.change_x = 0


# Запуск игры
if __name__ == "__main__":
    window = GameView()
    window.setup()
    arcade.run()