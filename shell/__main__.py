import gi
gi.require_version('Gtk', '3.0')

from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import Gtk

from .switcher import Switcher
from .launcher import Launcher

def main():
    DBusGMainLoop(set_as_default=True)
    Switcher()
    Launcher()
    Gtk.main()

main()
