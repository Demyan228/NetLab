import os
import sys
import pathlib

# parent_dir = str(pathlib.Path(__file__).resolve().parents[1])
# core_path = os.path.join(parent_dir, 'component_core')
# sys.path.insert(0, parent_dir)

from base_manager import BaseManager


class GUIManager(BaseManager):

    def __init__(self):
        super().__init__()
        with open('gui/m_init.txt', 'w') as f:
            print('GUI MANAGER INIT', file=f)


manager = GUIManager()
