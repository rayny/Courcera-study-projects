import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path

    def write(self, content):
        with open(self.path, 'w') as f:
            f.write(content)

    def __add__(self, other):
        res = os.path.join(tempfile.gettempdir(), 're_file.txt')
        with open(self.path, 'r') as f:
            with open(other.path, 'r') as g:
                new_obj = File(res)
                new_obj.write(f.read() + g.read())
        return new_obj

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.fope.__next__()
        except AttributeError:
            self.fope = open(self.path, 'r')
            return self.fope.__next__()
        except StopIteration:
            raise StopIteration

    def __str__(self):
        return self.path
