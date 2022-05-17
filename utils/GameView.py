import random
import typing

import arcade

from CardClass import Card
from utils.helpers import move_card_to_top

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
CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.5

PILE_COUNT = 15
BOTTOM_FACE_DOWN_PILE = 0
BOTTOM_FACE_UP_PILE_ONE = 1
BOTTOM_FACE_UP_PILE_TWO = 2
BOTTOM_FACE_UP_PILE_THREE = 3
PLAY_PILE_1 = 4
PLAY_PILE_2 = 5
PLAY_PILE_3 = 6
PLAY_PILE_4 = 7
PLAY_PILE_5 = 8
PLAY_PILE_6 = 9
PLAY_PILE_7 = 10
TOP_PILE_1 = 11
TOP_PILE_2 = 12
TOP_PILE_3 = 13
TOP_PILE_4 = 14
# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT


class Solitaire(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title=title)
        self.score = 0
        self.set_mouse_visible(False)

        self.card_list: typing.Optional[arcade.SpriteList, list] = []
        self.held_cards = []
        self.piles = []
        self.pile_list: arcade.SpriteList = arcade.SpriteList()

        self.background = None
        arcade.set_background_color((40, 192, 198))


    def setup(self) -> None:
        """
        Set up the game
        :return :class:`None`
        """
        self.card_list: typing.Optional[arcade.SpriteList, list] = []
        self.held_cards = []
        self.pile_list: arcade.SpriteList = arcade.SpriteList()
        self.card_list: arcade.SpriteList = arcade.SpriteList()

        for i in range(4):
            # Bottom row with extra cards
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.color_from_hex_string("#7F000000"))
            pile.position = START_X + (X_SPACING * i), BOTTOM_Y
            self.pile_list.append(pile)

        for i in range(7):
            # Middle playing piles
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.color_from_hex_string("#7F000000"))
            pile.position = START_X + i * X_SPACING, MIDDLE_Y
            self.pile_list.append(pile)

        for i in range(4):
            # Top foundation piles
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.color_from_hex_string("#7F000000"))
            pile.position = START_X + i * X_SPACING, TOP_Y
            self.pile_list.append(pile)

        for suit in _CARD_SUITES:
            for value in _CARD_VALUES:
                card = Card(suite=suit, number=value)
                card.position = START_X, BOTTOM_Y
                self.card_list.append(card)

        self.piles = [[] for _ in range(15)]  # For 13 elems, set to empty list.

        for position in range(len(self.card_list)):  # Randomize the cards
            self.card_list.swap(position, random.randrange(len(self.card_list)))
            # What random.randrange does is pick a random number between 0 and the length of the list.
            # It's different from random.randint, which picks a random number between two numbers. But this is inclusive.

        self.piles[BOTTOM_FACE_DOWN_PILE] = [i for i in self.card_list]

        for piles in range(PLAY_PILE_1, PLAY_PILE_7 + 1):
            for each in range(piles - PLAY_PILE_1 + 1):
                card: Card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()  # Remove from bottom face down pile and assigns to card
                self.piles[piles].append(card)  # Add to pile
                new_position = list(self.card_list[piles].position)
                new_position[1] -= CARD_VERTICAL_OFFSET * each  # Slightly move the card down
                """
                Tuples aren't really "changeable", so we need to convert the list to a tuple in order to
                modify the position.
                
                We also need to convert the tuple back to a list in order to assign it to the card as 
                position takes a tuple.
                """

                card.face_down()
                card.position = tuple(new_position)  # Set the new position

                self.pull_to_top(card)  # Pull the card to the top of the pile

        for i in range(PLAY_PILE_1, PLAY_PILE_7 + 1):
            self.piles[i][-1].face_up()  # Face up the top card of each pile
            # -1 is the last element in the list, so we face up the top card

    def on_draw(self):
        self.clear()
        self.pile_list.draw()
        self.card_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.setup()
        elif symbol == arcade.key.T:
            pass  # Todo: a way to finish the game without playing the game.

    def on_mouse_press(self, x, y, button, modifiers):
        cards: typing.Union[typing.List, arcade.SpriteList] = arcade.get_sprites_at_point((x, y), self.card_list)

        if not cards:
            return

        card: Card = cards[-1]  # Get the last card in the list, which is the top card of the pile

        if not isinstance(card, Card):
            # If the card is not a card, then scare the user.
            raise TypeError("The card at %x%y is not a Card object".replace("%x", str(x)).replace("%y", str(y)))

        pile_index = self.get_pile_for_card(card)

        if pile_index == BOTTOM_FACE_DOWN_PILE:
            for i in range(3):
                if (self.piles[BOTTOM_FACE_DOWN_PILE]) is None:
                    break
                if len(self.piles[BOTTOM_FACE_UP_PILE_ONE + i]) != 1:
                    continue  # Don't replace all the cards, only get new ones for those that are blank.
                card = self.piles[BOTTOM_FACE_DOWN_PILE][-1]
                card.face_up()
                card.position = self.pile_mat_list[BOTTOM_FACE_UP_PILE_ONE + i].position
                self.piles[BOTTOM_FACE_DOWN_PILE].remove(card)
                self.piles[BOTTOM_FACE_UP_PILE_ONE + i].append(card)
                self.pull_to_top(card)
        elif card.is_face_down:
            if self.piles[pile_index][-1] == card:
                card.face_up()  # If the card is the top card of the pile, then face it up
        # else:


    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def pull_to_top(self, card):
        self.card_list = move_card_to_top(self.card_list, card)


def main():
    game = Solitaire(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Solitaire")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
