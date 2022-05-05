import os
import typing

from archived.Cards.CardObjects.ace_of_clubs import AceOfClubs
from archived.Cards.CardObjects.ace_of_diamonds import AceOfDiamonds
from archived.Cards.CardObjects.ace_of_hearts import AceOfHearts
from archived.Cards.CardObjects.ace_of_spades import AceOfSpades
from archived.Cards.CardObjects.eight_of_clubs import EightOfClubs
from archived.Cards.CardObjects.eight_of_diamonds import EightOfDiamonds
from archived.Cards.CardObjects.eight_of_hearts import EightOfHearts
from archived.Cards.CardObjects.eight_of_spades import EightOfSpades
from archived.Cards.CardObjects.five_of_clubs import FiveOfClubs
from archived.Cards.CardObjects.five_of_diamonds import FiveOfDiamonds
from archived.Cards.CardObjects.five_of_hearts import FiveOfHearts
from archived.Cards.CardObjects.five_of_spades import FiveOfSpades
from archived.Cards.CardObjects.four_of_clubs import FourOfClubs
from archived.Cards.CardObjects.four_of_diamonds import FourOfDiamonds
from archived.Cards.CardObjects.four_of_hearts import FourOfHearts
from archived.Cards.CardObjects.four_of_spades import FourOfSpades
from archived.Cards.CardObjects.jack_of_clubs import JackOfClubs
from archived.Cards.CardObjects.jack_of_diamonds import JackOfDiamonds
from archived.Cards.CardObjects.jack_of_hearts import JackOfHearts
from archived.Cards.CardObjects.jack_of_spades import JackOfSpades
from archived.Cards.CardObjects.king_of_clubs import KingOfClubs
from archived.Cards.CardObjects.king_of_diamonds import KingOfDiamonds
from archived.Cards.CardObjects.king_of_hearts import KingOfHearts
from archived.Cards.CardObjects.king_of_spades import KingOfSpades
from archived.Cards.CardObjects.nine_of_clubs import NineOfClubs
from archived.Cards.CardObjects.nine_of_diamonds import NineOfDiamonds
from archived.Cards.CardObjects.nine_of_hearts import NineOfHearts
from archived.Cards.CardObjects.nine_of_spades import NineOfSpades
from archived.Cards.CardObjects.queen_of_clubs import QueenOfClubs
from archived.Cards.CardObjects.queen_of_diamonds import QueenOfDiamonds
from archived.Cards.CardObjects.queen_of_hearts import QueenOfHearts
from archived.Cards.CardObjects.queen_of_spades import QueenOfSpades
from archived.Cards.CardObjects.seven_of_clubs import SevenOfClubs
from archived.Cards.CardObjects.seven_of_diamonds import SevenOfDiamonds
from archived.Cards.CardObjects.seven_of_hearts import SevenOfHearts
from archived.Cards.CardObjects.seven_of_spades import SevenOfSpades
from archived.Cards.CardObjects.six_of_clubs import SixOfClubs
from archived.Cards.CardObjects.six_of_diamonds import SixOfDiamonds
from archived.Cards.CardObjects.six_of_hearts import SixOfHearts
from archived.Cards.CardObjects.six_of_spades import SixOfSpades
from archived.Cards.CardObjects.ten_of_clubs import TenOfClubs
from archived.Cards.CardObjects.ten_of_diamonds import TenOfDiamonds
from archived.Cards.CardObjects.ten_of_hearts import TenOfHearts
from archived.Cards.CardObjects.ten_of_spades import TenOfSpades
from archived.Cards.CardObjects.three_of_clubs import ThreeOfClubs
from archived.Cards.CardObjects.three_of_diamonds import ThreeOfDiamonds
from archived.Cards.CardObjects.three_of_hearts import ThreeOfHearts
from archived.Cards.CardObjects.three_of_spades import ThreeOfSpades
from archived.Cards.CardObjects.two_of_clubs import TwoOfClubs
from archived.Cards.CardObjects.two_of_diamonds import TwoOfDiamonds
from archived.Cards.CardObjects.two_of_hearts import TwoOfHearts
from archived.Cards.CardObjects.two_of_spades import TwoOfSpades
from CardClass import Card

name_mappings: typing.Final = {
    "hearts": "heart",
    "diamonds": "diamond",
    "spades": "spade",
    "clubs": "club",
}

number_mappings: typing.Final = {
    "ace": "ace",
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
    "king": "king",
}

color_mappings: typing.Final = {
    "heart": "red",
    "club": "black",
    "diamond": "red",
    "spade": "black",
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
        "color": color_mappings[name_mappings[__parts[2]]],
    }


yes = (
    TenOfClubs,
    TenOfDiamonds,
    TenOfHearts,
    TenOfSpades,
    TwoOfClubs,
    TwoOfDiamonds,
    TwoOfHearts,
    TwoOfSpades,
    ThreeOfClubs,
    ThreeOfDiamonds,
    ThreeOfHearts,
    ThreeOfSpades,
    FourOfClubs,
    FourOfDiamonds,
    FourOfHearts,
    FourOfSpades,
    FiveOfClubs,
    FiveOfDiamonds,
    FiveOfHearts,
    FiveOfSpades,
    SixOfClubs,
    SixOfDiamonds,
    SixOfHearts,
    SixOfSpades,
    SevenOfClubs,
    SevenOfDiamonds,
    SevenOfHearts,
    SevenOfSpades,
    EightOfClubs,
    EightOfDiamonds,
    EightOfHearts,
    EightOfSpades,
    NineOfClubs,
    NineOfDiamonds,
    NineOfHearts,
    NineOfSpades,
    AceOfClubs,
    AceOfDiamonds,
    AceOfHearts,
    AceOfSpades,
    JackOfClubs,
    JackOfDiamonds,
    JackOfHearts,
    JackOfSpades,
    KingOfClubs,
    KingOfDiamonds,
    KingOfHearts,
    KingOfSpades,
    QueenOfClubs,
    QueenOfDiamonds,
    QueenOfHearts,
    QueenOfSpades,
)


def init_cards() -> typing.List[Card]:
    """
    Returns a list of all the cards in the game
    :return:
    """
    current_directory = os.getcwd()
    os.chdir("..")
    cards = []
    for card in yes:
        cards.append(card())
    os.chdir(current_directory)
    return cards
