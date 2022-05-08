import typing


class Card:
    # instance = None
    def __init__(self, suite: str, number: typing.Union[str, int]):
        self.__suite: str = suite.title()  # ace / spade / heart / diamond
        self.__number: typing.Union[
            str, int
        ] = number  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / jack / queen / king
        self.__name: typing.Final[str] = f"{self.__number} of {self.__suite}"
        self.__asset_location: typing.Final[
            str
        ] = f"../assets/cards/{self.__number}_of_{self.__suite.lower()}s.png"

    def get_suite(self) -> str:
        """
        Returns the suite of the card
        :return: [:class:`str`]
        """
        return self.__suite

    def get_number(self) -> int:
        """
        Returns the number of the card
        :return: [:class:`int`]
        """
        return self.__number

    def get_name(self) -> str:
        """
        Returns the name of the card
        :return: [:class:`str`]
        """
        return self.__name

    def get_asset_location(self) -> str:
        """
        Returns the path of the card's asset
        :return: [:class:`str`]
        """
        return self.__asset_location

    def __repr__(self) -> str:
        """
        Represents the card as its name
        :return:
        """
        return f"<{self.__name}>"
