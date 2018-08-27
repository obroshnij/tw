import json
from .reader import Reader

class JsonParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        return json.loads(self.open_file())

    def open_file(self):
        return Reader(self.file).read()
