from libinput import KeyState

class Shortcuts:
    def __init__(self, switcher):
        self.switcher = switcher

    def handle(self, key, state):
        if key == 125 and state == KeyState.RELEASED:
            self.switcher.hide()
        if key == 15 and state == KeyState.PRESSED:
            self.switcher.show()
