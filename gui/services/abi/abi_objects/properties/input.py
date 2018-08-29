import re
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
    def defined_types_regex(self):
        types_regex_part = '|'.join(list(map(lambda x: f'({x})', self.__class__.defined_types())))
        return re.compile(fr'(?P<data_type>{types_regex_part})')

    @property
    def is_array(self):
        matched_data = self.array_regex.match(self.type)
        return matched_data and matched_data['array']

    @property
    def array_size(self):
        matched_data = self.array_regex.match(self.type)
        return matched_data and matched_data['num']

    @property
    def array_regex(self):
        return re.compile(r'.*?(?P<array>\[(?P<num>\d+)?\])$')

    @property
    def defined_type(self):
        matched_type = self.defined_types_regex.match(self.type)
        return matched_type and matched_type['data_type']

    @property
    def input_items(self):
        items = []
        sample_data = self.data.copy()
        sample_data['type'] = self.defined_type
        for i in range(int(self.array_size)):
            items.append(self.__class__(sample_data))
        return items

    @property
    def html_type(self):
        if self.defined_type in self.__class__.type_mapping():
            return self.__class__.type_mapping()[self.defined_type]
        else:
            return 'text'

    @staticmethod
    def type_mapping():
        return {
            'uint': 'number',
            'int': 'number',
            'address': 'number',
            'bytes': 'text',
            'bool': 'checkbox',
            'string': 'text',
            'function': 'number',
            'ufixed': 'number',
            'fixed': 'number'
        }

    @staticmethod
    def defined_types():
        return ['uint', 'int', 'address', 'bool', 'fixed', 'ufixed', 'bytes', 'function', 'string']
