import os
import typing
import main

from Cards.CardObjects.three_of_hearts import ThreeOfHearts
from Cards.CardObjects.two_of_hearts import TwoOfHearts

name_mappings: typing.Final = {
    "hearts": "heart",
    "diamonds": "diamond",
    "spades": "spade",
    "clubs": "club"
}

number_mappings: typing.Final = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

color_mappings: typing.Final = {
    "heart": "red",
    "club": "black",
    "diamond": "red",
    "spade": "black"
}


def get_types(filename: str) -> dict:
    """
    Returns a dict with the type of the card based on the file name

    Pass __file__, and this function will do the rest for you.
    :param filename: A string
    :return: A dict containing the values of the card which can be passed as a **kwargs to the Card class
    """
    __filename: str = os.path.basename(filename).split(".")[0]
    __parts: typing.List[str] = __filename.split("_")

    return {
        "number": number_mappings[__parts[0]],
        "suite": name_mappings[__parts[2]],
        "color": color_mappings[name_mappings[__parts[2]]]
    }


yes = (TwoOfHearts, ThreeOfHearts)
for card in yes:
    main.card_list.append(card())
print(main.card_list)
