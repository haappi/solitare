import typing

import arcade


class Card(arcade.Sprite):
    def __init__(self, suite: str, number: typing.Union[str, int], scale: typing.Union[int, float] = 1,):
        self.__suite: str = suite.title()  # ace / spade / heart / diamond
        self.__number: typing.Union[
            str, int
        ] = number  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / jack / queen / king
        self.__name: typing.Final[str] = f"{self.__number} of {self.__suite}"
        self.__asset_location: typing.Final[
            str
        ] = f"./assets/cards/{self.__number}_of_{self.__suite.lower()}.png"
        super().__init__(self.__asset_location, scale=scale, hit_box_algorithm="None")
        self.__is_face_up = False
        self.internal_number: typing.Final = int(self.__number.lower().replace("ace", "1").replace("jack", "11")
                                                 .replace("queen", "12").replace("king", "13"))

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
        :return: :class:`str`
        """
        return self.__asset_location

    def __repr__(self) -> str:
        """
        Represents the card as its name
        :return: [:class:`str`]
        """
        return f"<{self.__name}>"

    def set_card_face_down(self) -> None:
        """
        Sets the card face-down
        """
        self.__face_down()

    def set_card_face_up(self) -> None:
        """
        Sets the card face-up
        """
        self.__face_up()

    def __face_down(self) -> None:
        """
        Turn the card face-down
        :return: :class:`None`
        """
        self.texture = arcade.load_texture("../assets/cards/back.png")
        self.__is_face_up = False

    def __face_up(self) -> None:
        """
        Turn the card face-up
        :return: :class:`None`
        """
        self.texture = arcade.load_texture(self.__asset_location)
        self.__is_face_up = True

    @property
    def is_face_down(self) -> bool:
        """
        Returns whether the card is face-down
        :return: :class:`bool`
        """
        return not self.__is_face_up
