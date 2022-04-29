import typing
from utils import Card
import arcade



class CardSprite(arcade.Sprite):
    def __init__(self, asset: typing.Union[str, Card], scale: float = 1.0):
        if isinstance(asset, Card):
            asset = asset.get_asset_location()
        super().__init__(asset, scale)
