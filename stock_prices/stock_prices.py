#!/usr/bin/python

import argparse

def find_max_profit(prices):
  largest, smallest = 0, float('inf')
  temp_smallest = smallest
  for i in range(len(prices)):
    if prices[i] > largest and i > 0:
      largest, smallest = prices[i], temp_smallest
    if prices[i] < temp_smallest:
      temp_smallest = prices[i]
  return largest - smallest

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))