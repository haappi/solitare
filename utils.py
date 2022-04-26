import os
import random
import typing
from typing import Union

from PIL import Image


class Card:
    # instance = None
    def __init__(self, suite: str, number: typing.Union[str, int], color: str):
        self.__suite: str = suite.title()  # ace / spade / heart / diamond
        self.__number: typing.Union[
            str, int
        ] = number  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / jack / queen / king
        self.__color: str = color.title()  # red / black,
        self.__name: typing.Final[str] = f"{self.__number} of {self.__suite}"
        self.__asset_location: typing.Final[
            str
        ] = f"../assets/cards/{self.__number}_of_{self.__suite.lower()}s.png"

    def get_suite(self) -> str:
        return self.__suite

    def get_number(self) -> int:
        return self.__number

    def get_color(self) -> str:
        return self.__color

    def get_name(self) -> str:
        return self.__name

    def yes(self):
        return Image.open(self.__asset_location).show()

    def __repr__(self) -> str:
        return f"<{self.__name}>"
