from .controller import Controller

def Switcher(application):
    controller = Controller(application)
    controller.setup_shortcuts()
