import sys, getopt
import numpy as np
from math import ceil
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
    pairs = dict({']': '[', ')': '(', '}':'{', '>':'<'})
    scores = dict({']': 57, ')': 3, '}':1197, '>':25137})
    data = read_input("../inputs/" + inputfile)
    total_score = 0
    for i, line in enumerate(data):
      queue = []
      hist = []
      for s in line:
        hist.append(s)
        if s in open_symbols:
          queue.append(s)
        elif queue[-1] == pairs[s]:
              queue.pop(-1)
        else:
          # mismatch
          print('Corruption on line ', i,' : ', line)
          print(pairs[s], s, queue[-1])
          print(hist)
          total_score += scores[s]
          break
    print(total_score)


        

      
        

if __name__ == "__main__":
    main(sys.argv[1:])