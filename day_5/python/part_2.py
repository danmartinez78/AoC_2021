import sys, getopt
import numpy as np
from math import ceil
import copy



def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
        lines = [l.replace(" ", "") for l in lines]
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
    # print(data)
    occ = {}
    for line in data:
      line = line.split('->')
      x1, y1 = line[0].split(',')
      x2, y2 = line[1].split(',')
      # print(x1, ',', y1,'->',x2,',',y2 )
      if int(x1) == int(x2): # vertical
        # print('vertical line')
        for d in range(abs(int(y2)-int(y1))+1):
          y = min(int(y1),int(y2)) + d
          pos = x1 + ',' + str(y)
          # print('key', pos)
          if pos in occ:
            occ[pos] += 1
          else:
            occ[pos] = 1
          # print('key', pos, 'occ', occ[pos])
      elif int(y1) == int(y2): # horizontal
        # print('horizontal line')
        for d in range(abs(int(x2)-int(x1))+1):
          x = min(int(x1),int(x2)) + d
          pos = str(x) + ',' + y1
          # print('key', pos)
          if pos in occ:
            occ[pos] += 1
          else:
            occ[pos] = 1
          # print('key', pos, 'occ', occ[pos])
      else: # diagonal
        # print('diagonal line')
        if int(x1)<int(x2):
          x_values = range(int(x1), int(x2)+1, 1)
        else:
          x_values = range(int(x1), int(x2)-1, -1)
        if int(y1)<int(y2):
          y_values = range(int(y1), int(y2)+1)
        else:
          y_values = range(int(y1), int(y2)-1, -1)
        for x,y in zip([*x_values], [*y_values]):
          pos = str(x) + ',' + str(y)
          # print('key', pos)
          if pos in occ:
            occ[pos] += 1
          else:
            occ[pos] = 1
    
    count = 0
    for pos, density in occ.items():
      if density >=2:
        count += 1
    print(count)
    

if __name__ == "__main__":
    main(sys.argv[1:])