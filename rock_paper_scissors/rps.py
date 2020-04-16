#!/usr/bin/python

import sys

'''
base case = 0 number of plays left
create base lists of individual plays ie. [['rock'], ['paper'], ['scissors']]
loop through base case and add lists with one extra base instance till base == 0
return result
'''


def rock_paper_scissors(n):
    base = [['rock'], ['paper'], ['scissors']]
    result = []

    if n == 0:
        return [result]
    if n == 1:
        return base
    recursion = rock_paper_scissors(n-1)
    for times in recursion:
        for plays in base:
            result.append(times + plays)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
