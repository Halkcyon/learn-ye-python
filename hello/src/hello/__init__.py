__version__ = '0.1.0'


class Button:
    reserved: int | None

    def __init__(self):
        self.text = "some value"
        self.width = 10
        self.height = 10
        self.background_color = "white"
        self.foreground_color = "black"

        self.reserved = None


my_btn = Button()

my_btn.reserved = "string"
