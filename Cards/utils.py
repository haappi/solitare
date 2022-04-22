from typing import Union


class Card:
    # instance = None
    def __init__(self, suite: str, number: int, color: str):
        self.__suite = suite.title()  # ace / spade / hearts / diamond
        self.__number = number  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / jack / queen / king
        self.__color = color.title()  # red / black,
        self.__name = f"{self.__number} of {self.__suite}"

    def get_suite(self) -> str:
        return self.__suite

    def get_number(self) -> int:
        return self.__number

    def get_color(self) -> str:
        return self.__color

    def get_name(self) -> str:
        return self.__name
