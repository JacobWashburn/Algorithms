#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min = 100 ** 10
    max = 0
    min_index = 0
    for i in range(len(prices) - 1):
        if prices[i] < min:
            min, min_index = prices[i], i
    max_loop_list = prices[min_index + 1:]
    for v in max_loop_list:
        if v > max:
            max = v
    return max - min


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description = 'Find max profit from prices.')
    parser.add_argument('integers', metavar = 'N', type = int, nargs = '+', help = 'an integer price')
    args = parser.parse_args()

    print("\nA profit of ${profit} can be made from the stock prices {prices}.".format(
            profit = find_max_profit(args.integers), prices = args.integers))
