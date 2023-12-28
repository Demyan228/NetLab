import os
import sys
import pathlib

parent_dir = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, parent_dir)


from base_manager import BaseManager
from assembler.assembler import AssemblerComponent


class AssemblerManager(BaseManager):

    def __init__(self):
        super().__init__(AssemblerComponent())
        print('ASSEMBLER MANAGER INIT')
