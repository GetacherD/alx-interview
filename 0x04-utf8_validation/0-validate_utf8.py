#!/usr/bin/python3
"""
Validate UTF-8
"""


def validUTF8(data):
    """ validate UTF-8"""
    def bit_array(num):
        """ get bits array"""
        bitarr = bin(num)[2:]
        length = len(bitarr)
        padding = 8 - (length - (length // 8) * 8)
        if padding == 8:
            padding = 0
        return "0"*padding + bitarr

    byteArr = [bit_array(i) for i in data]
    print(" ".join(byteArr))
    i = 0
    while i < len(byteArr):
        by = byteArr[i]
        if by[:5] == "11110":
            i += 1
            for _ in range(3):
                if byteArr[i][:2] == "10":
                    i += 1
                else:
                    return False
        elif by[:4] == "1110":
            i += 1
            for _ in range(2):
                if byteArr[i][:2] == "10":
                    i += 1
                else:
                    return False
        elif by[:3] == "110":
            i += 1
            for _ in range(1):
                if byteArr[i][:2] == "10":
                    i += 1
                else:
                    return False
        elif by[0] == "0":
            i += 1
        else:
            return False
    return True
