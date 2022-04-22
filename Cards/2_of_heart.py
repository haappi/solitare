from Cards.utils import Card


class TwoOfHearts(Card):
    def __init__(self):
        super().__init__(suite='hearts', number=2, color='red')
        print(self.get_name())


TwoOfHearts()
