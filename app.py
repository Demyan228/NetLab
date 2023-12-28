from collections import defaultdict


class EventSystem:
    def __init__(self):
        self.subs = defaultdict(list)

    def invoke(self, event_type, event_data):
        for sub_addr in self.subs[event_type]:
            update_event(event_type, event_data, sub_addr)

    def subscribe(self, sub_addr, event_type):
        self.subs[event_type].append(sub_addr)


def update_event(event_type, event_data, apply_addr):
    pass


#transport 
def subscribe():
    pass


#transport 
def invoke():
    pass
