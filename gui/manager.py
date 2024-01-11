from base_manager import BaseManager


class GUIManager(BaseManager):

    def __init__(self):
        super().__init__()
        with open('gui/m_init.txt', 'w') as f:
            print('GUI MANAGER INIT', file=f)


manager = GUIManager()
