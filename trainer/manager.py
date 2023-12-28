import os
import sys
import pathlib

parent_dir = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, parent_dir)


from base_manager import BaseManager
from trainer.trainer import TrainerComponent


class TrainManager(BaseManager):

    def __init__(self):
        super().__init__(TrainerComponent())
        print('TRAINER MANAGER INIT')
