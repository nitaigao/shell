from shell.compositor import Compositor
from shell import keys

from os import system

class Controller:
    def __init__(self):
        compositor = Compositor()
        compositor.register_shortcut(keys.KEY_SPACE, keys.CTRL, keys.PRESSED, self.search)
        compositor.register_shortcut(keys.KEY_ENTER, keys.CTRL, keys.PRESSED, self.terminal)

    def search(self):
        system("launch2")

    def terminal(self):
        system("tilix")
