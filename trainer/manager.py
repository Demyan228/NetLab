from base_manager import BaseManager


class TrainManager(BaseManager):

    def __init__(self):
        super().__init__()
        print('TRAINER MANAGER INIT')


manager = TrainManager()
