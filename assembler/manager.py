from base_manager import BaseManager
from my_tools import log


class AssemblerManager(BaseManager):

    def __init__(self):
        super().__init__()
        log('ASSEMBLER MANAGER INIT')


manager = AssemblerManager()
