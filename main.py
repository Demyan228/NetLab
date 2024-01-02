from subprocess import Popen
from app import es
from time import sleep


def get_component_addres(ip, port):
    return f'{ip}:{port}'


PORT_START = 6100

componets = {
    'app': 'app.py',
    'gui': 'gui/gui.py',
    'assembler': 'assembler/assembler.py',
    'trainer': 'trainer/trainer.py',
}


prefix = 'python3'
server_ip = 'localhost'
server_addres = f'{server_ip}:{PORT_START}'

for port, cmd in enumerate(componets.values(), PORT_START):
    print(cmd, flush=True)
    addr = get_component_addres(ip='localhost', port=port)
    p = Popen([prefix, cmd, addr, server_addres])
    p.communicate()

sleep(5)
print('START', flush=True)
es.invoke('START_APP_EVENT', '')
