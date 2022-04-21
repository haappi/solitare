from typing import Union


class Card:
    # instance = None
    # todo singleton pattern
    def __init__(self, suite, number, color):
        self.suite = suite  # ace / spade / hearts / diamond
        self.number: Union[str, int] = number  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / jack / queen / king
        self.color = color  # red / black,
        self.name = f"{self.number} of {self.suite}"

