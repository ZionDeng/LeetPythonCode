# 连续打印

import sys


def fun(a):
    if len(a) > 8:
        print(a[:8])
        fun(a[8:])
    if len(a) <= 8:
        a += '0' * (8 - len(a))
        print(a)


for line in sys.stdin:
    fun(line.strip())
