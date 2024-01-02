from manager import manager


class AssemblerComponent():

    def __init__(self):
        print('ASSEMBLER COMPONENT INIT')
    
    def run(self, _):
        print('ASSEMBLER RUN')


assembler = AssemblerComponent()

manager.subscribe('START_APP_EVENT', assembler.run)
