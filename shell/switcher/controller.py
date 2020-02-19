from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import Gtk

from shell.compositor import Compositor
from shell.desktop_entry_store import DesktopEntryStore
from shell.input import Input
from shell.key_codes import Key, Modifier
from .view import View

class Controller:
    def __init__(self):
        self.compositor = Compositor()
        self.view = View()
        self.input = Input(self.on_key)
        self.showing = False
        self.store = DesktopEntryStore()
        self.entries = []
        self.selected_index = 0

    def setup_shortcuts(self):
        self.compositor.register_shortcut(Key.KEY_TAB, Modifier.ALT | Modifier.SHIFT, 1, lambda: self.backward())
        self.compositor.register_shortcut(Key.KEY_TAB, Modifier.ALT, 1, lambda: self.forward())

    def on_key(self, key_code, _state):
        if key_code == Key.KEY_LEFTALT:
            self.hide()

    def forward(self):
        apps = self.compositor.apps()
        self.entries = self.store.load_entries(apps)
        if not self.showing:
            self.selected_index = 1 if len(self.entries) > 1 else 0
            self.view.clear()
            self.view.populate(self.entries)
            self.showing = True
        else:
            self.selected_index += 1
            self.selected_index = 0 if self.selected_index >= len(self.entries) else self.selected_index
        self.view.show(self.selected_index)

    def backward(self):
        apps = self.compositor.apps()
        self.entries = self.store.load_entries(apps)
        if not self.showing:
            self.selected_index = len(self.entries) - 1
            self.view.clear()
            self.view.populate(self.entries)
            self.showing = True
        else:
            self.selected_index -= 1
            self.selected_index = len(self.entries) - 1 if self.selected_index < 0 else self.selected_index
        self.view.show(self.selected_index)

    def hide(self):
        if self.showing:
            focused_entry = self.entries[self.selected_index]
            self.compositor.focus(focused_entry.name)
            self.view.hide()
            self.showing = False
