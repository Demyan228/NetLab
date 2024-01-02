from base_manager import BaseManager


class AssemblerManager(BaseManager):

    def __init__(self):
        super().__init__()
        print('ASSEMBLER MANAGER INIT')


manager = AssemblerManager()
