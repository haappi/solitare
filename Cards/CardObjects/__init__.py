import os
import typing
import main

from Cards.CardObjects.ten_of_clubs import TenOfClubs
from Cards.CardObjects.ten_of_diamonds import TenOfDiamonds
from Cards.CardObjects.ten_of_hearts import TenOfHearts
from Cards.CardObjects.ten_of_spades import TenOfSpades
from Cards.CardObjects.two_of_clubs import TwoOfClubs
from Cards.CardObjects.two_of_diamonds import TwoOfDiamonds
from Cards.CardObjects.two_of_hearts import TwoOfHearts
from Cards.CardObjects.two_of_spades import TwoOfSpades
from Cards.CardObjects.three_of_clubs import ThreeOfClubs
from Cards.CardObjects.three_of_diamonds import ThreeOfDiamonds
from Cards.CardObjects.three_of_hearts import ThreeOfHearts
from Cards.CardObjects.three_of_spades import ThreeOfSpades
from Cards.CardObjects.four_of_clubs import FourOfClubs
from Cards.CardObjects.four_of_diamonds import FourOfDiamonds
from Cards.CardObjects.four_of_hearts import FourOfHearts
from Cards.CardObjects.four_of_spades import FourOfSpades
from Cards.CardObjects.five_of_clubs import FiveOfClubs
from Cards.CardObjects.five_of_diamonds import FiveOfDiamonds
from Cards.CardObjects.five_of_hearts import FiveOfHearts
from Cards.CardObjects.five_of_spades import FiveOfSpades
from Cards.CardObjects.six_of_clubs import SixOfClubs
from Cards.CardObjects.six_of_diamonds import SixOfDiamonds
from Cards.CardObjects.six_of_hearts import SixOfHearts
from Cards.CardObjects.six_of_spades import SixOfSpades
from Cards.CardObjects.seven_of_clubs import SevenOfClubs
from Cards.CardObjects.seven_of_diamonds import SevenOfDiamonds
from Cards.CardObjects.seven_of_hearts import SevenOfHearts
from Cards.CardObjects.seven_of_spades import SevenOfSpades
from Cards.CardObjects.eight_of_clubs import EightOfClubs
from Cards.CardObjects.eight_of_diamonds import EightOfDiamonds
from Cards.CardObjects.eight_of_hearts import EightOfHearts
from Cards.CardObjects.eight_of_spades import EightOfSpades
from Cards.CardObjects.nine_of_clubs import NineOfClubs
from Cards.CardObjects.nine_of_diamonds import NineOfDiamonds
from Cards.CardObjects.nine_of_hearts import NineOfHearts
from Cards.CardObjects.nine_of_spades import NineOfSpades
from Cards.CardObjects.ace_of_clubs import AceOfClubs
from Cards.CardObjects.ace_of_diamonds import AceOfDiamonds
from Cards.CardObjects.ace_of_hearts import AceOfHearts
from Cards.CardObjects.ace_of_spades import AceOfSpades
from Cards.CardObjects.jack_of_clubs import JackOfClubs
from Cards.CardObjects.jack_of_diamonds import JackOfDiamonds
from Cards.CardObjects.jack_of_hearts import JackOfHearts
from Cards.CardObjects.jack_of_spades import JackOfSpades
from Cards.CardObjects.king_of_clubs import KingOfClubs
from Cards.CardObjects.king_of_diamonds import KingOfDiamonds
from Cards.CardObjects.king_of_hearts import KingOfHearts
from Cards.CardObjects.king_of_spades import KingOfSpades
from Cards.CardObjects.queen_of_clubs import QueenOfClubs
from Cards.CardObjects.queen_of_diamonds import QueenOfDiamonds
from Cards.CardObjects.queen_of_hearts import QueenOfHearts
from Cards.CardObjects.queen_of_spades import QueenOfSpades

name_mappings: typing.Final = {
    "hearts": "heart",
    "diamonds": "diamond",
    "spades": "spade",
    "clubs": "club"
}

number_mappings: typing.Final = {
    "ace": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": "jack",
    "queen": "queen",
    "king": "king"
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


yes = (TenOfClubs, TenOfDiamonds, TenOfHearts, TenOfSpades, TwoOfClubs, TwoOfDiamonds, TwoOfHearts, TwoOfSpades, ThreeOfClubs, ThreeOfDiamonds, ThreeOfHearts, ThreeOfSpades, FourOfClubs, FourOfDiamonds, FourOfHearts, FourOfSpades, FiveOfClubs, FiveOfDiamonds, FiveOfHearts, FiveOfSpades, SixOfClubs, SixOfDiamonds, SixOfHearts, SixOfSpades, SevenOfClubs, SevenOfDiamonds, SevenOfHearts, SevenOfSpades, EightOfClubs, EightOfDiamonds, EightOfHearts, EightOfSpades, NineOfClubs, NineOfDiamonds, NineOfHearts, NineOfSpades, AceOfClubs, AceOfDiamonds, AceOfHearts, AceOfSpades, JackOfClubs, JackOfDiamonds, JackOfHearts, JackOfSpades, KingOfClubs, KingOfDiamonds, KingOfHearts, KingOfSpades, QueenOfClubs, QueenOfDiamonds, QueenOfHearts, QueenOfSpades)

for card in yes:
    main.card_list.append(card())
print(main.card_list)  # todo this prints twice. the first list looks inaccurate?
