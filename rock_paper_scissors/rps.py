#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  games = []
  def construct_games(cache=[]):
    if len(cache) == n: return games.append(cache)
    for choice in ['rock', 'paper', 'scissors']:
      construct_games(cache + [choice])
  construct_games()
  return games

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')