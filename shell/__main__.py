import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .input import Input
from .switcher import Switcher
from .shortcuts import Shortcuts

def main():
    switcher = Switcher()
    shortcuts = Shortcuts(switcher)
    input = Input(shortcuts)
    input.start()
    Gtk.main()

main()
