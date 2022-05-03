import typing

import arcade

_SCREEN_WIDTH: typing.Final[int] = 1024
_SCREEN_HEIGHT: typing.Final[int] = 768


class Solitaire(arcade.Window):
    def __init__(self):
        super().__init__(_SCREEN_WIDTH, _SCREEN_HEIGHT, "Solitaire")
        self.score = 0
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass


def main():
    game = Solitaire()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
