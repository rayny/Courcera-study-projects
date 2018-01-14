

class Container:
    cont = {}

    def __getitem__(self, item):
        return self.cont[item]

    def __setitem__(self, key, value):
        self.cont[key] = value
