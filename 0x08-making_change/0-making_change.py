#!/usr/bin/python3
"""
Make changes
"""


def makeChange(coins, total):
    """ make changes """
    if total == 0:
        return 0

    def combSum(candidates, target, index, cur, res):
        """ helper function """
        if target <= 0:
            if target == 0:
                res.append(cur[::])
            return
        if res:
            return
        if index < len(candidates):
            val = candidates[index]
            cur.append(val)
            combSum(candidates, target - val, index, cur, res)
            cur.pop()
            combSum(candidates, target, index + 1, cur, res)
        return res
    res = combSum(sorted(coins, reverse=True), total, 0, [], [])
    if res:
        return len(res[0])
    return -1
