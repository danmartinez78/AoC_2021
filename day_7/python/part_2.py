import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
        lines = [l.replace(" ", "") for l in lines]
        lines = [int(n) for n in lines[0].split(',')]
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
    pos = []
    costs = []
    for i in range(np.min(data), np.max(data)):
      pos.append(i)
      deltas = abs(data-i)
      ind_costs = (deltas*deltas + deltas)/2
      costs.append(np.sum(ind_costs))
    min_cost = min(costs)
    loc = np.where(costs == min_cost)[0][0]
    print(pos[loc], min_cost)
    

if __name__ == "__main__":
    main(sys.argv[1:])