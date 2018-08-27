from .json_parser import JsonParser
from .abi_object import AbiObject

def wrap(file):
    json_data = JsonParser(file).parse()
    return AbiObject.from_json(json_data)
