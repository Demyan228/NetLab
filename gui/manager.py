import os
import sys
import pathlib

parent_dir = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, parent_dir)

from base_manager import BaseManager
from gui.gui import GUIComponent


class GUIManager(BaseManager):

    def __init__(self):
        super().__init__(GUIComponent())
        print('GUI MANAGER INIT')
