#!/usr/bin/python3
"""
LOck Box
"""


def canUnlockAll(boxes):
    """ check if we can unlock all boxes"""
    size = len(boxes)
    visited = set()
    for i in boxes[0]:
        if i < size:
            visited.add(i)
    keys = set(boxes[0])
    tmp = set()
    len_visited = len(visited)
    while True:
        print(keys)
        for key in keys:
            if (key >= size):
                continue
            for k in boxes[key]:
                tmp.add(k)
                visited.add(k)
        if len(tmp) == 0:
            break
        if (len(visited) == len_visited):
            break
        keys = tmp.copy()
        tmp = set()
        len_visited = len(visited)
    visited.add(0)
    print("visited", visited)
    print("boxes", boxes)
    print(len(visited), len(boxes))
    if len(visited) == len(boxes):
        return True
    return False
