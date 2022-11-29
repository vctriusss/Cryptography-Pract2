from src.Byte import Byte
from typing import List, Any


class ByteString:
    bytes: List[Byte]

    def __init__(self, arg: Any):
        if isinstance(arg, List):
            self.bytes = arg
        elif isinstance(arg, Byte):
            self.bytes = [Byte(0)] * 15 + [arg]
        elif isinstance(arg, str):
            pairs = [arg[i * 2: i * 2 + 2] for i in range(len(arg) // 2)]
            self.bytes = list(map(lambda pair: Byte(int(pair, 16)), pairs))

    def __xor__(self, other):
        return ByteString([self.bytes[i] + other.bytes[i] for i in range(len(self.bytes))])

    def __getitem__(self, item: int):
        return self.bytes[item]

    def __str__(self):
        return ''.join([str(b) for b in self.bytes])
