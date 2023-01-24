#!/usr/bin/python3
"""
Validate UTF-8
"""


def validUTF8(data):
    """ validate UTF-8"""
    try:
        bytes(data).decode("UTF-8")
        return True
    except Exception:
        return False
