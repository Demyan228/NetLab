from subprocess import Popen
import os
from app import es
from pathlib import Path

os.environ["PYTHONPATH"] = os.path.join(Path(__file__).parent.absolute(), "component_core")



def get_component_addres(ip, port):
    return f'{ip}:{port}'


PORT_START = 6100

componets = {
    'app': 'app.py',
    'gui': 'gui/gui.py',
    'assembler': 'assembler/assembler.py',
    'trainer': 'trainer/trainer.py',
}


prefix = 'python'
server_ip = 'localhost'
server_addres = f'{server_ip}:{PORT_START}'

process_list = []

for port, cmd in enumerate(componets.values(), PORT_START):
    print(cmd, flush=True)
    addr = get_component_addres(ip='localhost', port=port)
    p = Popen([prefix, cmd, addr, server_addres])
    process_list.append(p)


for p in process_list:
    p.communicate()

print('START', flush=True)
es.invoke("START_APP_EVENT", "")