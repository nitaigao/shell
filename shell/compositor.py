import dbus

class Compositor:

    def run_shortcut(self, id):
        if id in self.shortcuts:
            self.shortcuts[id]()

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
