import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
        lines = [n.split(' | ') for n in lines]
        # lines = [l.replace(" ", "") for l in lines]
        
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
    print(data)

    counts = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(data)):
      for digit in data[i][1].split(' '):
        count = len(digit)
        if count == 2:
          counts[1] += 1
        elif count == 3:
          counts[7] += 1
        elif count == 4:
          counts[4] += 1
        elif count == 7:
          counts[8] += 1
    print(np.sum(counts))
   

if __name__ == "__main__":
    main(sys.argv[1:])