import os
import sys
import pathlib

parent_dir = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, parent_dir)

from base_manager import BaseComponent


class AssemblerComponent(BaseComponent):

    def __init__(self):
        print('ASSEMBLER COMPONENT INIT')
