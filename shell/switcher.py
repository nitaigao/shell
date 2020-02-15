import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Switcher:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_decorated(False);

    def show(self):
        self.window.show_all()

    def hide(self):
        self.window.hide()
