class SuperDict:
    def __init__(self):
        self.dict = dict()

    def add(self, key, value):
        if key in self.dict.keys():
            self.dict[key] += value
        else:
            self.dict[key] = value

    def subtract(self, key, value):
        self.add(key=key, value=-value)

    def keys(self):
        return self.dict.keys()

    def items(self):
        return self.dict.items()

    def values(self):
        return self.dict.values()

    def get(self, key):
        return self.dict[key]