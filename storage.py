class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise Exception

    def set(self, key, value):
        if key not in self.data.keys():
            raise Exception

        self.data[key] = value

    def add(self, key, value):
        if key in self.data:
            raise Exception
        else:
            self.data[key] = value
