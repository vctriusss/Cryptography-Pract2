import base64


def text_to_hex(text: str) -> str:
    new_text = text.encode().hex()
    new_text += '20' * ((32 - len(new_text)) % 32 // 2)
    return new_text


def hex_to_text(text: str) -> str:
    new_text = text + '20' * ((32 - len(text)) % 32 // 2)
    new_text = bytearray.fromhex(new_text).decode()
    return new_text


def text_to_base64(text: str) -> str:
    new_text = text.encode()
    new_text = base64.b64encode(new_text)
    new_text = new_text.decode()
    return new_text


def base64_to_text(text: str) -> str:
    new_text = text.encode()
    new_text = base64.b64decode(new_text)
    new_text = new_text.decode()
    return new_text


def hex_to_base64(text: str) -> str:
    new_text = text + '20' * ((32 - len(text)) % 32 // 2)
    new_text = base64.b64encode(bytes.fromhex(new_text)).decode()
    return new_text


def base64_to_hex(text: str) -> str:
    new_text = base64.b64decode(text.encode()).hex()
    new_text += '20' * ((32 - len(new_text)) % 32 // 2)
    return new_text


def hex_to_hex(text: str) -> str:
    return text + '20' * ((32 - len(text)) % 32 // 2)
