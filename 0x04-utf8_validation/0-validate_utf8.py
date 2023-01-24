#!/usr/bin/python3
"""
Validate UTF-8
"""


def validUTF8(data):
    """ validate UTF-8"""
    try:
        bits = [i & 255 for i in data]
        bytes(bits).decode("UTF-8")
        return True
    except Exception:
        return False
