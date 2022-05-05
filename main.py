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
"""

# 500 x 726

# from archived import Cards as CardObjects

card_list = []


# def init():
#     global card_list
#     card_list = CardObjects.init_cards()
#     print(card_list)


# init()

# https://reloadium.io/
