#!/usr/bin/python3
def validUTF8(data):
    n_bytes = 0
    for num in data:
        byte = num & 0xFF
        if n_bytes:
            if byte >> 6 != 2:
                return False
            n_bytes -= 1
            continue
        while (1 << abs(7 - n_bytes)) & byte:
            n_bytes += 1
        if n_bytes == 1 or n_bytes > 4:
            return False
        n_bytes = max(n_bytes - 1, 0)
    return n_bytes == 0
