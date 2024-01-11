# https://docs.python.org/3/howto/descriptor.html
import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        print(self, obj, objtype)
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname
 
s = Directory("full_stack")
s.size
