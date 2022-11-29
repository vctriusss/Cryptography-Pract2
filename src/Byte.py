class Byte:
    value: int

    def __init__(self, n: int):
        self.value = n

    def __add__(self, other):
        return Byte(self.value ^ other.value)

    def __iadd__(self, other):
        self.value ^= other.value
        return self

    def __mul__(self, other):
        other_value = other.value
        res = 0
        while self.value:
            if self.value & 1:
                res ^= other_value
            if other_value & 0x80:
                other_value = (other_value << 1) ^ 0x1C3
            else:
                other_value <<= 1
            self.value >>= 1
        return Byte(res)

    def __str__(self):
        hex_str = hex(self.value)[2:]
        return '0' * (2 - len(hex_str)) + hex_str
