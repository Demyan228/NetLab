from manager import manager
from my_tools import log


class TrainerComponent():

    def __init__(self):
        log('TRAINER COMPONENT INIT')
    
    def run(self, train_data):
        """
        train_data:
            model_path
            dataset_path
            hyperparams
        """
        log('TRAINER RUN')


trainer = TrainerComponent()

manager.subscribe('START_APP_EVENT', trainer.run)
