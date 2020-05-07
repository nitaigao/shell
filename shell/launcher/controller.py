from subprocess import Popen
from pathlib import Path

from shell.compositor import Compositor
from shell import keys

def run(command):
    Popen([command], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, cwd=Path.home())

def search():
    run("launch2")

def terminal():
    run("tilix")

class Controller:
    def __init__(self):
        compositor = Compositor()
        compositor.register_shortcut(keys.KEY_SPACE, keys.CTRL, keys.PRESSED, search)
        compositor.register_shortcut(keys.KEY_ENTER, keys.CTRL, keys.PRESSED, terminal)
