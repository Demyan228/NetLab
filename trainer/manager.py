from base_manager import BaseManager
from my_tools import log


class TrainManager(BaseManager):

    def __init__(self):
        super().__init__()
        log('TRAINER MANAGER INIT')


manager = TrainManager()
