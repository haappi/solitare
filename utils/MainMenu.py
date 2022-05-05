import arcade


class Instruction(arcade.View):
    """
    Make the buttons slide down as in some sort of smooth animation
    Make them slide up and down when they fully moved down

    Slide them out when closed with a smooth animation!

    https://api.arcade.academy/en/latest/examples/sprite_move_animation.html
    """
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
