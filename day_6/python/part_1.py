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
    for i in range(80):
      new_fish = []
      for index, age in enumerate(data):
        if age == 0:
          data[index] = 6
          new_fish.append(8)
        else:
          data[index] -= 1
      data += new_fish
      new_fish = []
      print(len(data))

if __name__ == "__main__":
    main(sys.argv[1:])