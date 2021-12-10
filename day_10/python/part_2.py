import sys, getopt
import numpy as np
from math import ceil, floor
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')

    return lines

def main(argv):
    try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
      print('part_1.py -i <inputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('part_1.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
    
    open_symbols = ['[', '(', '{', '<']
    close_pairs = dict({']': '[', ')': '(', '}':'{', '>':'<'})
    open_pairs = {value : key for (key, value) in close_pairs.items()}
    points = dict({']': 2, ')': 1, '}': 3, '>': 4})
    data = read_input("../inputs/" + inputfile)
    for i, line in enumerate(data[:]):
      queue = []
      hist = []
      for s in line:
        hist.append(s)
        if s in open_symbols:
          queue.append(s)
        elif queue[-1] == close_pairs[s]:
              queue.pop(-1)
        else:
          # mismatch
          data.remove(line)
          break
    scores = []
    for i, line in enumerate(data[:]):
      queue = []
      hist = []
      completion = []
      
      for s in line:
        hist.append(s)
        if s in open_symbols:
          queue.append(s)
        elif queue[-1] == close_pairs[s]:
              queue.pop(-1)
      #print(line, *queue)
      sat = []
      for s in queue:
        sat.insert(0, open_pairs[s])
      score = 0
      for s in sat:
        score*= 5
        score += points[s]
      scores.append(score)
    print(sorted(scores)[floor(len(scores)/2)])


if __name__ == "__main__":
    main(sys.argv[1:])