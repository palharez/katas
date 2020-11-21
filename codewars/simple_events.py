class Event():
    def __init__(self):
        self.emit_list = []
    
    def subscribe(self, f):
        self.emit_list.append(f)
    
    def unsubscribe(self, f):
        self.emit_list.remove(f)
    
    def emit(self, *args):
        for f in self.emit_list:
            f(*args)
