from django.test import TestCase
from .services.abi.abi_object import AbiObject

class AbiObjectTest(TestCase):
    @property
    def json_data(self):
        return [
                {
                    "constant": True,
                    "inputs":[],
                    "name":"ContractVersion",
                    "outputs":[{"name":"","type":"string"}],
                    "payable":False,
                    "stateMutability":"view",
                    "type":"function"
                },
                {
                    "constant":True,
                    "inputs":[{"name":"_hash","type":"bytes32"}],
                    "name":"getBytes32Value",
                    "outputs":[{"name":"","type":"bytes32"}],
                    "payable":False,
                    "stateMutability":"view",
                    "type":"function"
                }
            ]

    @property
    def instance(self):
        return AbiObject.from_json(self.json_data)

    def test_from_json(self):
        """Test correct instantiation of AbiObject and properties"""
        self.assertEqual(self.instance.properties[0].name, self.json_data[0]['name'])
        self.assertEqual(self.instance.properties[0].inputs, [])
        self.assertEqual(self.instance.properties[1].inputs[0].name, '_hash')
        self.assertEqual(self.instance.properties[1].inputs[0].type, 'bytes32')
        self.assertEqual(self.instance.properties[1].inputs[0].html_type, 'file')
