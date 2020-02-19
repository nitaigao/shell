import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, Pango

def setup_css_context():
    css = Gtk.CssProvider()
    css.load_from_data(str.encode('''
        .switcher {
            background-color: #333;
            border-radius: 5px;
            padding: 20px;
            color: #eee;
        }
        .tile {
            margin: 2px;
        }
        .highlight {
            border: 2px solid #ddd;
            border-radius: 5px;
        }
    '''))
    screen = Gdk.Screen.get_default()
    Gtk.StyleContext.add_provider_for_screen(screen, css,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class View:
    def __init__(self):
        setup_css_context()
        self.window = Gtk.Window()
        self.window.get_style_context().add_class("switcher")
        self.window.set_decorated(False);
        self.container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.window.add(self.container)

    def clear(self):
        children = self.container.get_children()
        for child in children:
            self.container.remove(child)

    def populate(self, entries):
        for entry in entries:
            tile = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            icon = Gtk.Image.new_from_icon_name(entry.getIcon(), Gtk.IconSize.DIALOG)
            icon.set_pixel_size(128)
            tile.add(icon)
            label = Gtk.Label(entry.getName())
            label.set_justify(Gtk.Justification.CENTER)
            label.set_ellipsize(Pango.EllipsizeMode.END)
            label.set_max_width_chars(15)
            label.set_margin_bottom(5)
            tile.add(label)
            tile.get_style_context().add_class('tile')
            self.container.add(tile)
        self.window.resize(1, 1)

    def show(self, selected_index):
        children = self.container.get_children()
        for i, tile in enumerate(children):
            if i == selected_index:
                tile.get_style_context().add_class('highlight')
                tile.get_style_context().remove_class('tile')
            else:
                tile.get_style_context().remove_class('highlight')
                tile.get_style_context().add_class('tile')
        self.window.show_all()

    def hide(self):
        self.window.hide()
