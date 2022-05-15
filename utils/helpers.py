import typing

import arcade

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


def stalk_pile_for_card(piles: typing.List, card: Card) -> typing.Union[int, None]:
    """
    Gets the pile a card is in.

    :param piles: The pile to search.
    :param card: The card to search for.
    :return: The pile the card is in.
    """
    # https://realpython.com/python-enumerate/
    # Basically how enumerate works.
    # It takes a list and returns a list of tuples. Each tuple contains the index and the value from the list.
    for index, pile in enumerate(piles):
        # index is the index of the pile. pile is the pile itself. It's split up like this because it's a tuple,
        # and python supports unpacking. (Splitting into multiple variables)
        if card in pile:
            return index
    return None
