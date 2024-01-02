from manager import manager


class TrainerComponent():

    def __init__(self):
        print('TRAINER COMPONENT INIT')
    
    def run(self, train_data):
        """
        train_data:
            model_path
            dataset_path
            hyperparams
        """
        print('TRAINER RUN')


trainer = TrainerComponent()

manager.subscribe('START_APP_EVENT', trainer.run)
