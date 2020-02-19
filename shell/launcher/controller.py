from shell.compositor import Compositor
from shell.key_codes import Key, Modifier

from os import system

class Controller:
    def __init__(self):
        compositor = Compositor()
        compositor.register_shortcut(Key.KEY_SPACE, Modifier.CTRL, 1, lambda: self.launch())

    def launch(self):
        system("launch2")
