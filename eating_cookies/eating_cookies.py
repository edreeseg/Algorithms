#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# def eating_cookies(n, cache=None):
#   if n < 0: return 0
#   if n == 0: return 1
#   return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
  if n == 0: return 1
  cache = [1] + [0] * n
  for i in range(1, n+1):
    total = 0
    for j in range(1, 4):
      if i-j >= 0:
        total += cache[i-j]
    cache[i] = total
  return cache[n]

print(eating_cookies(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')