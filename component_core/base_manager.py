import sys
from collections import defaultdict
import json
import requests
from flask import Flask, request


class BaseManager:

    def __init__(self):
        self.app = Flask(__name__)
        self.apply_addr = sys.argv[1] + '/update'
        self.server_addr = sys.argv[2]
        self.update_event = self.app.route('/update')(self._update_event)
        self.addres = sys.argv[1]
        self.ip, self.port = self.addres.split(':')
        self.events_handlers = defaultdict(list)
        self.run()

    def run(self):
        self.app.run('localhost', port=int(self.port))

    def _update_event(self):
        json_content = request.get_json()
        event_type = json_content['event_type']
        event_data = json_content['event_data']
        for event_handler in self.events_handlers[event_type]:
            event_handler(event_data)
        return '', 200

    def subscribe(self, event_type, event_handler):
        self.events_handlers[event_type].append(event_handler)
        self._subscribe(event_type)

    def _subscribe(self, event_type):
        data = json.dumps(
                    {
                        'event_type': event_type,
                        'apply_addr': self.apply_addr,
                    }
                )
        url = f'{self.server_addr}/subscribe'
        requests.post(url, json=data)

    def invoke(self, event_type, event_data):
        data = json.dumps(
                    {
                        'event_type': event_type, 
                        'event_data': event_data,
                    }
                )
        url = f'{self.server_addr}/{self.invoke}'
        requests.post(url, json=data)

