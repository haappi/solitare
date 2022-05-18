"""
https://www.wikihow.com/Play-Solitaire
https://www.wikihow.com/Win-at-Solitaire
- 4 long piles.

p    y x x x x x x  [hearts]
a      y x x x x x  [diamonds]
a        y x x x x  [clubs]
a          y x x x  [spades]
             y x x
               y x
                 y
    []

stuff
cards can only go to cards that are
- higher number
- different color

p = extra pile cards
a = cards from extra pile
- only face up
- max of 3

kings > queens > jacks > 10s > 9s > 8s > 7s > 6s > 5s > 4s > 3s > 2s > aces
only kings can be in empty spaces

aces can start the extra card pile on the right side

- returned to bottom of deck
y = cards that are face up
x = cards that are face down
[a] = cards that are face up and are in the ace piles
[] = cards that are face down and are in the extras pile

# Make sure that the game has some sort of creative twist. Nothing that can be *easily* found on the internet.

# todo thing to make so game auto compltes
-  score function
-  finishing game sequence
-  show the ascpets of the code
-  REWRIRE THE CODE
"""
import pprint
import random
import typing

import arcade

from CardClass import Card

"""
go through tthe entire code
show all the aspects of the code within the program without showing the code

"""

# 500 x 726

# Constants
# "Borrowed" from https://api.arcade.academy/en/latest/tutorials/card_game/solitaire_11.html#solitaire-11
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Constants for sizing
CARD_SCALE = 0.6

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = (MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT)

RIGHT_X = (SCREEN_WIDTH - MAT_WIDTH / 2 - MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT) - 50

# The Y of the top row (4 piles)
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The Y of the middle row (7 piles)
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

# If we fan out cards stacked on each other, how far apart to fan them?
CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.5

CARD_NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITES = ["Clubs", "Hearts", "Spades", "Diamonds"]

piles: typing.Final[typing.Dict[str, int]] = {
    "count": 15,
    "main": 0,
    "face_up_1": 1,
    # "face_up_2": 2,
    # "face_up_3": 3,
    "play_1": 4,
    "play_2": 5,
    "play_3": 6,
    "play_4": 7,
    "play_5": 8,
    "play_6": 9,
    "play_7": 10,
    "foundation_1": 11,
    "foundation_2": 12,
    "foundation_3": 13,
    "foundation_4": 14,
}


class Done(arcade.Window):
    def __int__(self):
        super().__init__()

    def on_draw(self):
        self.clear()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print("i've been summoned")


class Solitaire(arcade.Window):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)

        arcade.set_background_color((40, 192, 198))  # light blue

        self.card_list = arcade.SpriteList()
        self.held_cards = []
        self.held_cards_original_position = []
        self.pile_mat_list = arcade.SpriteList()
        # self.piles: typing.List[typing.List[Card]] = []
        self.piles = []

    def setup(self):
        # Clear everything
        self.partial_setup()

        # for suit in CARD_SUITES:
        #     for number in CARD_NUMBERS:
        #         card = Card(suit, number, (START_X, BOTTOM_Y), CARD_SCALE)
        #         self.card_list.append(card)
        random.shuffle(CARD_SUITES)
        random.shuffle(CARD_NUMBERS)
        card_list = [Card(suit, number, (START_X, BOTTOM_Y), CARD_SCALE)
                     for suit in CARD_SUITES
                     for number in CARD_NUMBERS]
        # random.sample shuffles in place, so we need to make a new list for the one liner.
        # BUT- it's slower by 0.00000001 ms so i care.
        self.card_list.extend(card_list)  # What extend does is add all the elements of the list to the sprite list.
        # Like append but all at once. Instead of chained append.

        self.piles[piles['main']] = [card for card in self.card_list]

        # We need to fill the piles from left-right, top-bottom.
        # Right having the most

        for pile in range(piles['play_1'], piles['play_7'] + 1):
            for tall in range(pile + 1 - piles['play_1']):
                thy_card: Card = self.piles[piles['main']].pop()
                self.piles[pile].append(thy_card)

                thy_card.set_position(self.pile_mat_list[pile].center_x, self.pile_mat_list[pile].center_y)
                thy_card.set_position(thy_card.center_x, (thy_card.center_y - (tall * CARD_VERTICAL_OFFSET)))
                self.pull_to_top(thy_card)

        for i in range(piles['play_1'], piles['play_7'] + 1):
            self.piles[i][-1].face_up()

    def on_draw(self):
        self.clear()
        self.pile_mat_list.draw()
        self.card_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.setup()
        if symbol == arcade.key.T:
            self.cheat_test()

    def pull_to_top(self, card: Card) -> None:
        """
        Moves a card to the top of a pile.

        :param card: The card to move.
        :return: [:class:`None`] It's in-place, bozo.
        """
        self.card_list.remove(card)
        self.card_list.append(card)

    def __remove_card_from_pile(self, card: Card) -> None:
        """
        Removes a card from a pile.

        :param card: The card to remove.
        :return: [:class:`None`] It's in-place, bozo.
        """
        for pile in self.piles:
            try:
                pile.remove(card)
            except ValueError:  # Throws if the card isn't in the pile. Let's just ignore it.
                pass

    def __get_pile_for_card(self, card) -> int:
        """
        Gets the pile a card is in.

        :param card: The card to search for.
        :return: The pile the card is in.
        """
        # https://realpython.com/python-enumerate/
        # Basically how enumerate works.
        # It takes a list and returns a list of tuples. Each tuple contains the index and the value from the list.
        for index, pile in enumerate(self.piles):
            # index is the index of the pile. pile is the pile itself. It's split up like this because it's a tuple,
            # and python supports unpacking. (Splitting into multiple variables)
            if card in pile:
                return index

    def __move_card(self, card: Card, pile: int) -> None:
        """
        Moves a card to a new pile.

        :param card: The card to move.
        :param pile: The pile to move the card to.
        :return: [:class:`None`] It's in-place, bozo.
        """
        self.__remove_card_from_pile(card)
        self.piles[pile].append(card)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for card in self.held_cards:  # We wanna do this for all the cards.
            # card.center_x += dx
            # card.center_y += dy  # Move the card with the mouse.
            card.set_position(card.center_x + dx, card.center_y + dy)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Wait I need to make a docstring for this?
        :param x:
        :param y:
        :param button:
        :param modifiers:
        :return:
        """
        cards = arcade.get_sprites_at_point((x, y), self.card_list)
        if not cards:
            return

        first_boi = cards[-1]

        if not isinstance(first_boi, Card):
            mats = arcade.get_sprites_at_point((x, y), self.pile_mat_list)

            if len(mats) > 0:
                mat = mats[0]
                mat_index = self.pile_mat_list.index(mat)

                if mat_index == piles['main'] and len(self.piles[piles['main']]) == 0:
                    temp_list = self.piles[piles['face_up_1']].copy()
                    for card in reversed(temp_list):
                        card.face_down()
                        self.piles[piles['face_up_1']].remove(card)
                        self.piles[piles['main']].append(card)
                        card.position = self.pile_mat_list[piles['main']].position

        index = self.__get_pile_for_card(first_boi)

        if index == piles['main']:
            for i in range(3):
                if len(self.piles[piles['main']]) == 0:
                    break
                if len(self.piles[piles['face_up_1'] + i]) != 0:
                    continue  # Skip that pile.
                card = self.piles[piles['main']].pop(-1)
                self.piles[piles['face_up_1'] + i].append(card)
                self.pull_to_top(card)
                card.set_card_face_up()
                card.set_position(self.pile_mat_list[piles['face_up_1'] + i].center_x,
                                  self.pile_mat_list[piles['face_up_1'] + i].center_y)
                return
        elif first_boi.is_face_down:
            if self.__get_pile_for_card(first_boi) == index:
                # print(self.piles[index][-1])
                if self.piles[index][-1] == first_boi:
                    first_boi.face_up()
                return
        else:
            self.held_cards.clear()
            self.held_cards.append(first_boi)
            self.held_cards_original_position = [first_boi.position]
            self.pull_to_top(first_boi)

            better_index = self.piles[index].index(first_boi)
            for i in range(better_index + 1, len(self.piles[index])):
                card: Card = self.piles[index][i]
                self.held_cards.append(card)
                self.pull_to_top(card)
                self.held_cards_original_position.append(card.position)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """
        I need more docstrings?????????????
        :param x:
        :param y:
        :param button:
        :param modifiers:
        :return:
        """

        if not self.held_cards:
            return  # Nothing to do.

        # Get the closet sprite at the mouse position.
        # arcade.get_closest_sprite returns a tuple with two objects.
        # The first is the sprite, the second is the distance.
        card, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)

        can_move = False

        index = self.pile_mat_list.index(card)
        if index == self.__get_pile_for_card(self.held_cards[0]):
            for card in self.held_cards:
                card.position = self.held_cards_original_position[self.held_cards.index(card)]
                self.held_cards.remove(card)
            self.held_cards = []
        elif index in range(piles['play_1'], piles['play_7'] + 1):  # MAIN PILES.
            # Construct a range list to see if it's in-range
            if self.piles[index]:
                top_most: Card = self.piles[index][-1]
                if top_most.can_be_stacked_ugh(top_most, self.held_cards[0]):
                    # print("Can stack")
                    can_move = True
                    for _index, _card in enumerate(self.held_cards):
                        _card.set_position(top_most.center_x, top_most.center_y - CARD_VERTICAL_OFFSET * (_index + 1))
                else:
                    can_move = False
                    # print("LLLL")
            else:
                if self.held_cards[0].get_number() == "K":
                    can_move = True
                    bap: Card = self.held_cards.pop(0)
                    bap.set_position(self.pile_mat_list[index].center_x, self.pile_mat_list[index].center_y)
                    print(bap)
                    for _index, _card in enumerate(self.held_cards):
                        _card.set_position(bap.center_x, bap.center_y - CARD_VERTICAL_OFFSET * (_index + 1))
                    # print("Is a king")

        elif index in range(piles['foundation_1'], piles['foundation_4'] + 1):  # FOUNDATION.
            if self.piles[index]:
                if self.held_cards[0].can_be_on_foundation(self.piles[index][-1]):
                    can_move = True
                    for _index, _card in enumerate(reversed(self.held_cards)):
                        _card.set_position(card.center_x, card.center_y)
                        self.pull_to_top(_card)
            else:
                # print(self.held_cards)
                if self.held_cards[-1].get_number() == "A":
                    can_move = True
                    for _index, _card in enumerate(reversed(self.held_cards)):
                        _card.set_position(self.pile_mat_list[index].center_x, self.pile_mat_list[index].center_y)
                        self.pull_to_top(_card)
            # if len(self.piles[index]) == 0:
            #     if self.held_cards[-1].get_suite() == "A":
            #         can_move = True
            #         for _index, _card in enumerate(self.held_cards):
            #             _card.set_position(self.pile_mat_list[index].center_x, self.pile_mat_list[index].center_y)
            # # can_move = True
            # for _index, _card in enumerate(self.held_cards):
            #     _card.set_position(self.pile_mat_list[index].center_x, self.pile_mat_list[index].center_y)

        if not can_move:
            for card in self.held_cards:
                card.position = self.held_cards_original_position[self.held_cards.index(card)]
                self.held_cards.remove(card)
        for card in self.held_cards:
            self.__move_card(card, index)

        self.held_cards = []
        # if self.check_win():
        #     img = arcade.load_texture('bob.png')
        #     arcade.start_render()
        #     arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, img)
        #     arcade.finish_render()
        #     print("shown")

    def check_win(self):
        if len(self.piles[piles['foundation_1']]) == 13 and len(self.piles[piles['foundation_2']]) == 13 and \
                len(self.piles[piles['foundation_3']]) == 13 and len(self.piles[piles['foundation_4']]) == 13:
            return True
        return False

    def cheat_test(self):
        self.partial_setup()

        CARD_SUITES = ["Clubs", "Hearts", "Spades", "Diamonds"]
        CARD_NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        card_list = [Card(suit, number, (START_X, BOTTOM_Y), CARD_SCALE)
                     for suit in CARD_SUITES
                     for number in CARD_NUMBERS]

        self.card_list.extend(card_list)
        self.piles[piles['main']] = [card for card in self.card_list]

        for i in range(4):
            for x in range(13):
                a_card: Card = self.piles[piles['main']].pop()
                a_card.face_up()
                self.piles[i + 4].append(a_card)
                a_card.set_position(self.pile_mat_list[i + 4].center_x, self.pile_mat_list[i + 4].center_y)
                a_card.set_position(a_card.center_x, (a_card.center_y - (x * CARD_VERTICAL_OFFSET)))
                self.pull_to_top(a_card)

    def partial_setup(self):
        """
        Some duplicated code setup.
        :return:
        """
        self.held_cards_original_position = []
        self.held_cards = []
        self.pile_mat_list = arcade.SpriteList()
        self.card_list = arcade.SpriteList()
        self.piles = [[] for _ in range(piles['count'])]

        for i in range(4):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.color_from_hex_string("#7F000000"))
            pile.position = START_X + (X_SPACING * i), BOTTOM_Y
            self.pile_mat_list.append(pile)

        for i in range(7):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.color_from_hex_string("#7F000000"))
            pile.position = START_X + i * X_SPACING, MIDDLE_Y
            self.pile_mat_list.append(pile)

        for i in range(4):
            pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.color_from_hex_string("#7F000000"))
            pile.position = RIGHT_X, TOP_Y - (i * X_SPACING * 1.5)
            self.pile_mat_list.append(pile)


def main():
    # Start with 720p screen resolution
    window = Solitaire(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, name="Solitaire")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
# https://reloadium.io/
