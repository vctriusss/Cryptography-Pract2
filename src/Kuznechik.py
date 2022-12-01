from src.Byte import Byte
from src.ByteString import ByteString
from typing import Tuple, List
from src.converter import *


class Kuznechik:
    text: List[ByteString]
    new_text: List[str]
    key: str
    keys = List[ByteString]
    input_enc: str
    output_enc: str

    def __init__(self, input_enc: str, output_enc: str):
        self.input_enc = input_enc
        self.output_enc = output_enc
        self.new_text = []
        with open('input.txt', 'r', encoding='utf-8') as f:
            input_text = f.read()
            input_text = self.converter(input_text, self.input_enc, 'hex')
            self.text = [ByteString(input_text[32 * i: 32 * i + 32]) for i in range(len(input_text) // 32)]

        with open('key.txt', 'r', encoding='utf-8') as keyf:
            self.key = keyf.read()
            self.keys = [ByteString(self.key[:32]), ByteString(self.key[32:])]
            self.generate_iterkeys()

    def write_new(self):
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(self.converter(''.join(self.new_text), 'hex', self.output_enc))

    @classmethod
    def converter(cls, text: str, origin: str, to: str):
        if origin == 'text':
            if to == 'hex':
                return text_to_hex(text)
            if to == 'base64':
                return text_to_base64(text)
        if origin == 'hex':
            if to == 'text':
                return hex_to_text(text)
            if to == 'base64':
                return hex_to_base64(text)
            if to == 'hex':
                return hex_to_hex(text)
        if origin == 'base64':
            if to == 'text':
                return base64_to_text(text)
            if to == 'hex':
                return base64_to_hex(text)

    PI_LIST = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46,
               153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66,
               139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44,
               81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191,
               114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158,
               178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169,
               62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220,
               232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65,
               173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172,
               29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144,
               202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
               116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)

    PI_REV_LIST = (165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145, 100, 3, 87, 90, 28, 96, 7,
                   24, 33, 114, 168, 209, 41, 198, 164, 63, 224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229,
                   66, 228, 21, 183, 200, 6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213, 195,
                   175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47, 155, 67, 239, 217, 121, 182,
                   83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162, 223, 166, 254, 172, 34, 249, 226, 74, 188, 53,
                   202, 238, 120, 5, 107, 81, 225, 89, 163, 242, 113, 86, 17, 106, 137, 148, 101, 140, 187, 119, 60,
                   123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 219, 105, 179, 20, 149,
                   190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 55, 97, 75, 185, 227, 186, 241, 160, 133, 131,
                   218, 71, 197, 176, 51, 250, 150, 111, 110, 194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125, 236,
                   88, 247, 31, 251, 124, 9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 235, 248, 243, 62, 61,
                   189, 138, 136, 221, 205, 11, 19, 152, 2, 147, 128, 144, 208, 36, 52, 203, 237, 244, 206, 153, 16,
                   68, 64, 146, 58, 1, 38, 18, 26, 72, 104, 245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116)

    def generate_iterkeys(self):
        for i in range(1, 5):
            key2, key1 = self.keys[-2], self.keys[-1]
            for j in range(1, 9):
                key2, key1 = self.F(self.C(8 * (i - 1) + j), key2, key1)
            self.keys.append(key2)
            self.keys.append(key1)

    def l(self, bs: ByteString) -> Byte:
        consts = (148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1)
        res = Byte(0)
        for i in range(16):
            res += (Byte(consts[i]) * bs[i])
        return res

    def X(self, k: ByteString, a: ByteString) -> ByteString:
        return k ^ a

    def S(self, bs: ByteString, inverse=False) -> ByteString:
        if not inverse:
            res = [Byte(self.PI_LIST[bs[i].value]) for i in range(16)]
        else:
            res = [Byte(self.PI_REV_LIST[bs[i].value]) for i in range(16)]
        return ByteString(res)

    def R(self, bs: ByteString, inverse=False) -> ByteString:
        if not inverse:
            res = [self.l(bs)] + bs[:-1]
        else:
            res = bs.bytes[1:] + [self.l(ByteString(bs[1:] + [bs[0]]))]
        return ByteString(res)

    def L(self, bs: ByteString, inverse=False) -> ByteString:
        for _ in range(16):
            bs = self.R(bs, inverse)
        return bs

    def F(self, k: ByteString, a1: ByteString, a0: ByteString) -> Tuple[ByteString, ByteString]:
        return self.L(self.S(self.X(k, a1))) ^ a0, a1

    def C(self, i: int) -> ByteString:
        return self.L(ByteString(Byte(i)))

    def LSX(self, key: ByteString, bs: ByteString, inverse=False) -> ByteString:
        if not inverse:
            return self.L(self.S(self.X(key, bs)))
        else:
            return self.S(self.L(self.X(key, bs), inverse), inverse)

    def encrypt(self):
        for block in self.text:
            bs = block
            for i in range(9):
                bs = self.LSX(self.keys[i], bs)
            bs = self.X(self.keys[9], bs)
            self.new_text.append(str(bs))
        self.write_new()

    def decrypt(self):
        for block in self.text:
            bs = block
            for i in range(9, 0, -1):
                bs = self.LSX(self.keys[i], bs, inverse=True)
            bs = self.X(self.keys[0], bs)
            self.new_text.append(str(bs))
        self.write_new()


