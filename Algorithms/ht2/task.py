# умножение, crc 32

def str_key(string):
    code = ''
    for i in string:
        code += str(ord(i))
    return int(code)


def bin_str_key(string):
    return ' '.join(format(ord(i), 'b') for i in string)


def multiplication(key_s):
    hash_s = []
    M = len(key_s)
    C = 0.6180339887
    for i in key_s:
        if type(i) == str:
            key = str_key(i)
            hash_s.append((((key * C) % 1) * M) // 1)
        else:
            hash_s.append((((i * C) % 1) * M) // 1)
    return hash_s


def crc32(data):
    poly = 0xEDB88320
    crc = 0xFFFFFFFF
    data_bytes = bytearray(data, 'utf-8')
    for byte in data_bytes:
        for bit in range(8):
            if (crc ^ (byte >> bit)) & 0x00000001:
                crc = (crc >> 1) ^ poly
            else:
                crc = crc >> 1
    return '{:08X}'.format(crc)










