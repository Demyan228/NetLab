import json
from subprocess import Popen
import os
from time import sleep
from pathlib import Path
import requests


os.environ["PYTHONPATH"] = os.path.join(Path(__file__).parent.absolute(), "component_core")



def get_component_addres(ip, port):
    return f'{ip}:{port}'

def send_start_event():
    data = {
            'event_type': "START_APP_EVENT",
            'event_data': "",
        }
    url = f'{server_addres}/invoke'
    requests.post(url, json=data)


PORT_START = 6100

componets = {
    'gui': 'gui/gui.py',
    'assembler': 'assembler/assembler.py',
    'trainer': 'trainer/trainer.py',
}


prefix = 'python'
server_ip = 'localhost'
server_addres = f'http://{server_ip}:{PORT_START}'

process_list = []
app = Popen([prefix, "app.py", server_ip, str(PORT_START)])
sleep(2)

for port, cmd in enumerate(componets.values(), PORT_START + 1):
    print(cmd, flush=True)
    addr = get_component_addres(ip='localhost', port=port)
    p = Popen([prefix, cmd, addr, server_addres])

sleep(1)
print('START', flush=True)
#send_start_event()
sleep(100)

#app.communicate()