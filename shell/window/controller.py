from shell.compositor import Compositor
from shell import keys

class Controller:
    def __init__(self):
        compositor = Compositor()
        compositor.register_shortcut(keys.KEY_LEFT, keys.ALT,
                                     keys.PRESSED, compositor.dock_left)
        compositor.register_shortcut(keys.KEY_RIGHT, keys.ALT,
                                     keys.PRESSED, compositor.dock_right)
        compositor.register_shortcut(keys.KEY_UP, keys.ALT,
                                     keys.PRESSED, compositor.maximize)
        compositor.register_shortcut(keys.KEY_DOWN, keys.ALT,
                                     keys.PRESSED, compositor.minimize)
