import gi
gi.require_version('Gtk', '3.0')

from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import Gtk

from .launcher import Launcher
from .switcher import Switcher
from .window import Window

def main():
    DBusGMainLoop(set_as_default=True)
    Switcher()
    Launcher()
    Window()
    Gtk.main()

main()
