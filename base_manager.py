from abc import ABC, abstractmethod


class BaseComponent(ABC):
    def __init__(self, subscribe_handler, invoke_handler):
        pass

    @abstractmethod
    def update_event(self, event_type, event_data): ...


class BaseManager:

    def __init__(self, component: BaseComponent):
        pass

    def run(self):
        pass

    def subscribe(self, event_type):
        pass

    def invoke(self, event_type, event_data):
        pass
