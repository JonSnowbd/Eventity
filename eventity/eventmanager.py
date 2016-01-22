class EventManager(object):
    def __init__(self):
        self.subscriptions = []

    def on(self, event_string, fn):
        subscription = {
            "trigger": event_string,
            "fn": fn
        }
        self.subscriptions.append(subscription)

    def trigger(self, event_string, data = {}):
        for sub in self.subscriptions:
            if sub["trigger"] == event_string:
                sub["fn"](data)
