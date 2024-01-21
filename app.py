import sys
from collections import defaultdict
import sys
import json
import requests
from flask import Flask, request
from my_tools import log


log('START IN APP')

class EventSystem:
    def __init__(self):
        self.subs = defaultdict(list)

    def invoke(self, event_type, event_data):
        for sub_addr in self.subs[event_type]:
            update_event(event_type, event_data, sub_addr)
            log(sub_addr)

    def subscribe(self, sub_addr, event_type):
        with open("eslog.txt", "a") as file:
            self.subs[event_type].append(sub_addr)
            file.write(f"{sub_addr} || {event_type}\n")


def update_event(event_type, event_data, apply_addr):
    data ={
            "event_type": event_type,
            "event_data": event_data,
        }
    requests.post(apply_addr, json=data)


app = Flask(__name__)
es = EventSystem()


@app.route("/invoke", methods=['POST'])
def invoke():
    data = request.json
    es.invoke(event_type=data["event_type"], event_data=data["event_data"])
    return "", 200


@app.route("/subscribe", methods=['POST'])
def subscribe():
    data = request.json
    sub_addr = data["apply_addr"]
    event_type = data["event_type"]
    print(f'ES SUB: {sub_addr} || {event_type}', flush=True)
    es.subscribe(sub_addr, event_type)
    return "", 200


if __name__ == '__main__':
    addr, port = sys.argv[1], sys.argv[2]
    app.run(addr, int(port))



