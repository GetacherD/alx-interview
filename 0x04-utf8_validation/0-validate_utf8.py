#!/usr/bin/python3
"""
Validate UTF-8
"""


def validUTF8(data):
    """ validate UTF-8"""
    try:
        bitsarr = [i & 255 for i in data]
        bytes(bitsarr).decode("UTF-8")
        return True
    except Exception:
        return False
