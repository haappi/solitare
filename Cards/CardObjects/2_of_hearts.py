from Cards import CardObjects
from utils import Card


class TwoOfHearts(Card):
    def __init__(self):
        super().__init__(**CardObjects.get_types(__file__))
