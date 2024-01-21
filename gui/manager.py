from base_manager import BaseManager
from my_tools import log


class GUIManager(BaseManager):

    def __init__(self):
        super().__init__()
        log('GUI MANAGER INIT')


manager = GUIManager()
