#!/usr/bin/python3
"""
LOck Box
"""


def canUnlockAll(boxes):
    """ check if we can unlock all boxes"""
    set_prev = set(boxes[0])
    set_prev.add(0)
    set_next = set_prev.copy()
    len_prev = len(set_prev)
    len_next = len(set_next)
    while True:
        for i in set_next:
            for key in boxes[i]:
                set_prev.add(key)
        len_next = len(set_prev)
        if (len_next == len_prev):
            break
        set_next = set_prev.copy()
        len_prev = len(set_prev)
    if len(set_prev) == len(boxes):
        return True
    return False
