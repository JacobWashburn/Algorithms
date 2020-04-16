#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache = None, position = 'start'):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    amount = eating_cookies(n - 1, cache, '-1') + eating_cookies(n - 2, cache, '-2') + eating_cookies(n - 3, cache, '-3')
    cache[n] = amount
    return amount


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n}"
              " cookies.".format(ways = eating_cookies(num_cookies, None, 'start'), n = num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
