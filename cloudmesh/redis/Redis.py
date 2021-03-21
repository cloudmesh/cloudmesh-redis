

class Redis:
    def __init__(self, host=None, user=None, port=None, dir=None):
        self.host = host
        self.user = user
        self.port = port
        self.dir = dir



    def start(self):
        print(self.host)

    def stop(self):
        pass
