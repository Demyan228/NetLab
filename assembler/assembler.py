from manager import manager
from my_tools import log


class AssemblerComponent():

    def __init__(self):
        log('ASSEMBLER COMPONENT INIT')
    
    def run(self, _):
        log('ASSEMBLER RUN')


assembler = AssemblerComponent()

manager.subscribe('START_APP_EVENT', assembler.run)
