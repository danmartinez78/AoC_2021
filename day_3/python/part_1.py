import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().splitlines()
        lines = [list(line) for line in lines]
        for i in range(len(lines)):
          lines[i] = list(map(int, lines[i]))
    return lines

def find_most_least_common(data):
  gamma = ''
  epsilon = ''
  data = np.asarray(data)
  count = np.sum(data, axis = 0)
  result = count >= ceil(data.shape[0]/2)
  gamma = [int(x) for x in result]
  epsilon = [int(x) for x in [not elem for elem in result]]
  gamma = [str(intgr) for intgr in gamma]
  epsilon = [str(intgr) for intgr in epsilon]
  return ''.join(gamma), ''.join(epsilon)


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
    gamma, epsilon = find_most_least_common(copy.copy(data))
    print(gamma, epsilon)
    print(int(gamma, 2) * int(epsilon, 2))



if __name__ == "__main__":
    main(sys.argv[1:])