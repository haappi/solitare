import typing

import arcade
from arcade import SpriteList

from CardClass import Card


def yeet_card_from_pile(piles: typing.List, card: Card) -> typing.List:
    """
    Removes a card from a pile.

    :param piles: The pile to remove the card from.
    :param card: The card to remove.
    :return: The original pile with the card removed.
    """
    for pile in piles:
        if card in pile:  # If the card is in the pile
            pile.remove(card)  # Remove the card from the pile
            return pile  # Return the pile with the card removed




def move_card_to_top(piles: arcade.SpriteList, card: Card) -> SpriteList:
    """
    Moves a card to the top of a pile.

    :param piles: The pile to move the card to.
    :param card: The card to move.
    :return: The pile with the card at the end of the pile.
    """
    piles.remove(card)
    piles.append(card)
    return piles
