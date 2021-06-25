#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): list of integers

    Returns:
        Boolean: True if data is a valid UTF-8 encoding, else False
    """
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
