import arcade


class Solitaire(arcade.View):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)