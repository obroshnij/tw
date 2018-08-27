import pdb
from .abi_objects.property import Property

class AbiObject:
    def __init__(self):
        self.properties = []

    def populate_from_json(self, json_data):
        for data_item in json_data:
            if data_item == None:
                continue
            self.properties.append(self.build_property(data_item));

    def build_property(self, property_item):
        return Property(property_item)

    @classmethod
    def from_json(klass, json_data):
        instance = klass()
        instance.populate_from_json(json_data)
        return instance
