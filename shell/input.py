from libinput import LibInput, ContextType, EventType, KeyState
from gi.repository.GLib import idle_add
from threading import Thread

class Input:
    def __init__(self, handler):
        self.handler = handler
        self.thread = Thread(target=self.run, args=())
        self.thread.start()

    def run(self):
        li = LibInput(context_type=ContextType.UDEV)
        li.assign_seat('seat0')
        for event in li.events:
            self.process_event(event)

    def process_event(self, event):
        if event.type == EventType.KEYBOARD_KEY:
            idle_add(self.handler, event.key, event.key_state)
