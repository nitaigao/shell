import dbus

class Compositor:
    def run_shortcut(self, shortcut_id):
        if shortcut_id in self.shortcuts:
            self.shortcuts[shortcut_id]()

    def __init__(self):
        self.shortcuts = {}
        self.proxy = dbus.SessionBus().get_object('org.os.Compositor', '/org/os/Compositor')
        self.shortcut = dbus.Interface(self.proxy, 'org.os.Compositor.Shortcut')
        self.window = dbus.Interface(self.proxy, 'org.os.Compositor.Window')
        self.shortcut.connect_to_signal("Shortcut", self.run_shortcut)

    def register_shortcut(self, key_code, modifiers, state, action):
        shortcut_id = self.shortcut.Register(key_code, modifiers, state)
        self.shortcuts[shortcut_id] = action

    def apps(self):
        return self.window.Apps()

    def focus(self, app):
        self.window.Focus(app)

    def dock_left(self):
        self.window.DockLeft()

    def dock_right(self):
        self.window.DockRight()

    def maximize(self):
        self.window.Maximize()

    def minimize(self):
        self.window.Minimize()
