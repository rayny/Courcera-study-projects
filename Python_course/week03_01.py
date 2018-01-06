

class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            f = open(self.path, 'r')
            return f.read()
        except IOError:
            return ""

