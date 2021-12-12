import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
        lines = [list(l) for l in lines]
        lines = [list(map(int, n)) for n in lines]
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
    
    data = read_input("../inputs/" + inputfile)
    data = np.asarray(data)
    print(data)
    height_map = {}
    h = len(data)
    w = len(data[0])
    risks = []
    for r in (range(h)):
      for c in (range(w)):
        value = data[r][c]
        low = True
        if (r!=0):
          # up valid
          low = value < data[r-1][c] and low
        if (r!=h-1):
          # down valid
          low = value < data[r+1][c] and low
        if (c!=0):
          # left valid
          low = value < data[r][c-1] and low
        if (c!=w-1):
          # right valid
          low = value < data[r][c+1] and low
        if low:
          print(r,c,value)
          risks.append(value +1)
    print(np.sum(risks))

        

      
        

if __name__ == "__main__":
    main(sys.argv[1:])