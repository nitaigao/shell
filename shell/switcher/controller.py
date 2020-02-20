from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import Gtk

from shell.compositor import Compositor
from shell.desktop_entry_store import DesktopEntryStore
from shell.input import Input
from shell import keys
from .view import View

class Controller:
    def __init__(self):
        self.compositor = Compositor()
        self.view = View()
        self.input = Input(self.on_key)
        self.store = DesktopEntryStore()
        self.visible = False
        self.entries = []
        self.selected_index = 0

    def setup_shortcuts(self):
        self.compositor.register_shortcut(keys.KEY_TAB, keys.ALT | keys.SHIFT, keys.PRESSED, self.backward)
        self.compositor.register_shortcut(keys.KEY_TAB, keys.ALT, keys.PRESSED, self.forward)

    def on_key(self, key_code, _state):
        if key_code == keys.KEY_LEFTALT:
            self.hide()

    def forward(self):
        apps = self.compositor.apps()
        self.entries = self.store.load_entries(apps)
        if not self.visible:
            self.selected_index = 1 if len(self.entries) > 1 else 0
            self.view.clear()
            self.view.populate(self.entries)
            self.visible = True
        else:
            self.selected_index += 1
            self.selected_index = 0 if self.selected_index >= len(self.entries) else self.selected_index
        self.view.show(self.selected_index)

    def backward(self):
        apps = self.compositor.apps()
        self.entries = self.store.load_entries(apps)
        if not self.visible:
            self.selected_index = len(self.entries) - 1
            self.view.clear()
            self.view.populate(self.entries)
            self.visible = True
        else:
            self.selected_index -= 1
            self.selected_index = len(self.entries) - 1 if self.selected_index < 0 else self.selected_index
        self.view.show(self.selected_index)

    def hide(self):
        if self.visible:
            focused_entry = self.entries[self.selected_index]
            self.compositor.focus(focused_entry.name)
            self.view.hide()
            self.visible = False
