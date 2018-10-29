#!/usr/bin/env python3

import collections
import sys


def kolakoski(n):
    yield 1
    yield 2
    n -= 2

    cache = collections.deque((2, ))
    while n > 0:
        first = cache.popleft()
        yield first

        last = None
        try:
            last = cache[-1]
        except IndexError:
            last = 2

        for _ in range(first):
            cache.append(1 if last == 2 else 2)

        n -= 1


if __name__ == '__main__':
    n = None
    try:
        n = int(sys.argv[1])
    except (ValueError, IndexError):
        print("Usage: {} <length>".format(sys.argv[0]), file=sys.stderr)
        exit(1)

    for v in kolakoski(n):
        print(v)
