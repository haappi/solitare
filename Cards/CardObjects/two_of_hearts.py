from Cards import CardObjects
from utils import Card


class TwoOfHearts(Card):
    def __init__(self):
        super().__init__(**CardObjects.get_types(__file__))

    def __new__(cls, *args, **kwargs):
        print("Two of Hearts")
        return super().__new__(cls, *args, **kwargs)
