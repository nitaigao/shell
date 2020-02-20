from glob import glob

from xdg.DesktopEntry import DesktopEntry
from os.path import basename

class DesktopEntryStore:
    APPS_PATH_SYSTEM = "/usr/share/applications/"

    def __init__(self):
        all_entries = glob(f"{DesktopEntryStore.APPS_PATH_SYSTEM}/*.desktop")
        self.entries = list(map(DesktopEntry, all_entries))

    def load_entries(self, apps):
        all_entries = list(map(self.find_entry, apps))
        entries = [i for i in all_entries if i]
        return entries

    def find_entry(self, app):
        for entry in self.entries:
            if basename(entry.filename) == f"{app}.desktop" or entry.getStartupWMClass() == app:
                entry.name = app
                return entry
