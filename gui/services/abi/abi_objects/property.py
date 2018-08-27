import pdb
from .properties.input import Input

class Property:
    def __init__(self, data):
        self.data = data

    @property
    def is_function(self):
        return self.data['type'] == 'function'

    @property
    def is_constructor(self):
        return self.data['type'] == 'constructor'

    @property
    def is_event(self):
        return self.data['type'] == 'event'

    @property
    def name(self):
        if 'name' in self.data:
            return self.data['name']
        elif self.is_constructor():
            return 'Constructor'
        else:
            return '_'

    @property
    def inputs(self):
        if 'inputs' in self.data:
            return list([Input(x) for x in self.data['inputs']])
