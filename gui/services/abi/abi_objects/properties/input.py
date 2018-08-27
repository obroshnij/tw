import pdb

class Input:
    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data['name']

    @property
    def type(self):
        return self.data['type']

    @property
    def html_type(self):
        if self.type:
            return self.__class__.type_mapping()[self.type]
        else:
            return 'text'

    @staticmethod
    def type_mapping():
        return {
            'uint256': 'number',
            'address': 'number',
            'address[]': 'number',
            'bytes32': 'file',
            'bytes': 'file',
            'bytes32[]': 'file',
            'bool': 'checkbox',
            'uint8': 'number',
            'int64': 'number',
            'string': 'text'
        }
