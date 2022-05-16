import typing

import arcade


class Card(arcade.Sprite):
    def __init__(self, suite: str, number: typing.Union[str, int], scale: typing.Union[int, float] = 1):

        self.__suite: str = suite.title()  # ace / spade / heart / diamond
        self.__number: typing.Union[
            str, int
        ] = number  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / jack / queen / king
        self.__name: typing.Final[str] = f"{self.__number} of {self.__suite}"
        # self.__asset_location: typing.Final[
        #     str
        # ] = f"../assets/cards/{self.__number}_of_{self.__suite.lower()}s.png"
        self.__asset_location: typing.Final[str] = f":resources:images/cards/card{self.__suite}{self.__number}.png"
        self.__color: typing.Final[str] = 'black' if self.__suite.lower() in ('spade', 'club') else 'red'
        super().__init__(self.__asset_location, scale=scale, hit_box_algorithm="None")
        self.__is_face_up = False
        self.__internal_number: typing.Final = int(self.__number.lower().replace("a", "1").replace("j", "11")
                                                   .replace("q", "12").replace("k", "13"))

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
        self.face_down()

    def set_card_face_up(self) -> None:
        """
        Sets the card face-up
        """
        self.__face_up()

    def face_down(self) -> None:
        """
        Turn the card face-down
        :return: :class:`None`
        """
        self.texture = arcade.load_texture(":resources:images/cards/cardBack_red2.png")
        self.__is_face_up = False

    def __face_up(self) -> None:
        """
        Turn the card face-up
        :return: :class:`None`
        """
        self.texture = arcade.load_texture(self.__asset_location)
        self.__is_face_up = True

    def face_up(self) -> None:
        """
        Turn the card face-up
        :return: :class:`None`
        """
        self.__face_up()

    def get_internal_number(self) -> int:
        """
        Returns the internal number of the card
        :return: [:class:`int`]
        """
        return self.__internal_number

    @property
    def is_face_down(self) -> bool:
        """
        Returns whether the card is face-down
        :return: :class:`bool`
        """
        return not self.__is_face_up

    def can_be_stacked(self, other: 'Card') -> bool:
        """
        Returns whether the card can be stacked on the other card
        :param other: Union[:class:`Card`, :class:`None`] The other card
        :return: [:class:`bool`] whether the card can be stacked on the other card
        """
        print(other)
        print(self)
        # print((not other.is_face_down) or ((self.get_internal_number() < other.get_internal_number()) and (self.__color != other.__color)))
        return (not other.is_face_down) or ((self.get_internal_number() < other.get_internal_number()) and (self.__color != other.__color))
        # return (self.__internal_number <= other.__internal_number) and (self.__color != other.__color) or (other is None)

    def can_be_on_foundation(self, preceding: typing.Union[None, 'Card']) -> bool:
        """
        Returns whether the card can be on the foundation
        :param preceding: Union[:class:`Card`, :class:`None`] the top that is on the foundation
        :return: [:class:`bool`] whether the card can be on the foundation
        """
        print(preceding)
        if not preceding:
            return True
        return (self.__internal_number == preceding.__internal_number + 1) \
            and (self.__color == preceding.__color) \
            and (self.__suite == preceding.__suite)
