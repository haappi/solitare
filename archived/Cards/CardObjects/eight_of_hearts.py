from archived.Cards import CardObjects
from CardClass import Card


class EightOfHearts(Card):
    def __init__(self):
        super().__init__(**CardObjects.get_types(__file__))

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
