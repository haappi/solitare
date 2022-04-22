import os.path

from Cards import CardObjects
from Cards.utils import Card


class TwoOfHearts(Card):
    def __init__(self):
        super().__init__(suite='heart', number=2, color='red')


# TwoOfHearts().yes()
print(CardObjects.get_types(__file__))