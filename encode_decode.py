def encode(my_str : str):
    if not isinstance(my_str, str) or set(my_str) <= {'0', '1'}:
        raise TypeError(f"str excepted {type(my_str)} found")
    return "".join([f"{i:08b}" for i in bytearray(my_str, 'utf-8') if len(chr(i).encode()) == 1 ])


def decode(my_str : str):
    if not isinstance(my_str, str) or len({'0', '1'}.intersection(set(my_str))) == 0:
        raise TypeError(f"str excepted {type(my_str)} found")
    return "".join([chr(int(my_str[i:i+8], 2)) for i in range(0, len(my_str), 8)])