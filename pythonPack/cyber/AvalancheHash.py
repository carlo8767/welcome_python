
import hashlib

class TestAvalancheEffect:

    def convertBinary(self, value):
        ord(value)


    def test_avalance_effect(self):
        byte_input1 = bytearray("Hello World1", 'utf-8')
        byte_input2 = bytearray("Hello World1", 'utf-8')
        list_different = list()

        binary_list1 = [format(byte, '08b') for byte in byte_input1]
        binary_list2 = [format(byte, '08b') for byte in byte_input2]
        ns = [int(x) ^ int(y) for x, y in zip(binary_list2, binary_list1)]
        hashValue1 = hashlib.sha256(byte_input1).hexdigest()
        hashValue2 = hashlib.sha256(byte_input2).hexdigest()




