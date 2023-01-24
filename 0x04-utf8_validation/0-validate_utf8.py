#!/usr/bin/python3
"""
Validate UTF-8
"""


def validUTF8(data):
    """ validate UTF-8"""

    byteArr = [bin((i & 255))[2:] for i in data]
    bts = [i.zfill(8) for i in byteArr]
    print(bts)
    i = 0
    lng = len(bts)
    while i < len(bts):
        by = bts[i]
        if by[:5] == "11110":
            i += 1
            for _ in range(3):
                if i >= lng:
                    return False
                if bts[i][:2] == "10":
                    i += 1
                else:
                    return False
        elif by[:4] == "1110":
            i += 1
            for _ in range(2):
                if i >= lng:
                    return False
                if bts[i][:2] == "10":
                    i += 1
                else:
                    return False
        elif by[:3] == "110":
            i += 1
            for _ in range(1):
                if i >= lng:
                    return False
                if bts[i][:2] == "10":
                    i += 1
                else:
                    return False
        elif by[0] == "0":
            i += 1
        else:
            return False
    return True
