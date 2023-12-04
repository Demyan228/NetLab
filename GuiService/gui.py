from LocalTransport import transport


transport.invoke("event_name", {})
transport.create("event_name")

@transport.subscribe("event_name")
def fun(params):
    pass


