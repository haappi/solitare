import typing

import arcade

from CardClass import Card

_SCREEN_WIDTH: typing.Final[int] = 1200
_SCREEN_HEIGHT: typing.Final[int] = 800
_CARD_SUITES = ["Spades", "Hearts", "Diamonds", "Clubs"]
_CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
MAT_PERCENT_OVERSIZE = 1.25
CARD_SCALE = 0.6
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT


# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT
class Solitaire(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title=title)
        self.score = 0
        self.card_list: typing.Optional[arcade.SpriteList, list] = []
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self) -> None:
        """
        Set up the game
        :return :class:`None`
        """
        for i in range(7):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = START_X + i * X_SPACING, MIDDLE_Y
            self.pile_mat_list.append(pile)

        for i in range(4):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = START_X + i * X_SPACING, TOP_Y
            self.pile_mat_list.append(pile)
        # self.card_list = arcade.SpriteList()
        # for suit in _CARD_SUITES:
        #     for value in _CARD_VALUES:
        #         card = Card(suite=suit, number=value)

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
