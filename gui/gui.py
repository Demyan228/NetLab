from manager import manager


class GUIComponent():

    def __init__(self):
        with open('gui/init.txt', 'w') as f:
            print('GUI COMPONENT INIT', file=f)
    
    def run(self, _):
        with open('gui/run.txt', 'w') as f:
            print('GUI RUN', file=f)


gui = GUIComponent()


manager.subscribe('START_APP_EVENT', gui.run)
