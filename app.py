import sys
from collections import defaultdict
import json
from time import sleep

import requests
from flask import Flask, request


class EventSystem:
    def __init__(self):
        self.subs = defaultdict(list)

    def invoke(self, event_type, event_data):
        for sub_addr in self.subs[event_type]:
            update_event(event_type, event_data, sub_addr)

    def subscribe(self, sub_addr, event_type):
        with open('eslog.txt', 'a') as file:
            self.subs[event_type].append(sub_addr)
            file.write(f'{sub_addr} || {event_type}\n')


def update_event(event_type, event_data, apply_addr):
    data = json.dumps(
        {
            "event_type": event_type,
            "event_data": event_data,
        }
    )

    requests.post(apply_addr, json=data)


app = Flask(__name__)
es = EventSystem()

@app.route("/subscribe")
def subscribe():
    data = request.get_json()
    sub_addr = data["apply_addr"]
    event_type = data["event_type"]
    print(f'ES SUB: {sub_addr} || {event_type}', flush=True)
    es.subscribe(sub_addr, event_type)
    return "", 200


@app.route("/invoke")
def invoke():
    data = request.get_json()
    es.invoke(event_type=data["event_type"], event_data=data["event_data"])
    return "", 200


if __name__ == '__main__':
    app.run("localhost", port=5234)



