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
    pop = [0,0,0,0,0,0,0,0,0]
    for left in data:
      pop[left] += 1
      print(pop)
    for i in range(256):
      new_pop = [0,0,0,0,0,0,0,0,0]
      new_pop[8] = pop[0]
      new_pop[7] = pop[8]
      new_pop[6] = pop[0] + pop[7]
      new_pop[5] = pop[6]
      new_pop[4] = pop[5]
      new_pop[3] = pop[4]
      new_pop[2] = pop[3]
      new_pop[1] = pop[2]
      new_pop[0] = pop[1]
      pop = new_pop
      print(pop, np.sum(pop))

if __name__ == "__main__":
    main(sys.argv[1:])