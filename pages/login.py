from flet import *
from utils.colors import *

class Login(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = deepurple