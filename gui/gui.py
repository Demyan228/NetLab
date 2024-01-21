from manager import manager
from my_tools import log


class GUIComponent():

    def __init__(self):
        log('GUI COMPONENT INIT')
    
    def run(self, _):
        log('GUI RUN')


gui = GUIComponent()


manager.subscribe('START_APP_EVENT', gui.run)
