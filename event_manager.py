class EventManager:

    def __init__(self):
        self.events = {}

    def register_event(self, event_name, callback):

        if event_name not in self.events:
            self.events[event_name] = []

        self.events[event_name].append(callback)

        print(f"✅ Event Registered: {event_name}")

    def trigger_event(self, event_name, *args, **kwargs):

        if event_name not in self.events:
            print(f"⚠️ No Listeners For: {event_name}")
            return

        print(f"\n🚀 Event Triggered: {event_name}")

        for callback in self.events[event_name]:
            callback(*args, **kwargs)

    def list_events(self):

        return list(self.events.keys())

    def remove_event(self, event_name):

        if event_name in self.events:
            del self.events[event_name]
            print(f"✅ Event Removed: {event_name}")
        else:
            print("❌ Event Not Found")


event_manager = EventManager()