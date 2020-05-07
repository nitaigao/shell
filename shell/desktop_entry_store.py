from glob import glob

from os.path import basename
from xdg.DesktopEntry import DesktopEntry


def entry_matches(entry, app):
    if basename(entry.filename) == f"{app}.desktop":
        return True

    if (
        entry.getStartupWMClass() is not None
        and entry.getStartupWMClass().lower() == app.lower()
    ):
        return True

    if entry.getName() == app:
        return True
    return False


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
            if entry_matches(entry, app):
                entry.name = app
                return entry
