import typing

import arcade

from utils import Card

_SCREEN_WIDTH: typing.Final[int] = 1024
_SCREEN_HEIGHT: typing.Final[int] = 768
_CARD_SUITES = ["Spades", "Hearts", "Diamonds", "Clubs"]
_CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Solitaire(arcade.Window):
    def __init__(self):
        super().__init__(_SCREEN_WIDTH, _SCREEN_HEIGHT, "Solitaire")
        self.score = 0
        self.card_list = None
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self) -> None:
        """
        Set up the game
        :return :class:`None`
        """
        self.card_list = arcade.SpriteList()
        for suit in _CARD_SUITES:
            for value in _CARD_VALUES:
                card = Card(suite=suit, number=value)

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
