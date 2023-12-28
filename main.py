from subprocess import Popen


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
    addr = get_component_addres(ip='localhost', port=port)
    p = Popen([prefix, cmd, addr, server_addres])
    p.communicate()
