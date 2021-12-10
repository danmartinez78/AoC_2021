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
    low_points = []
    neighbors_map = {}
    value_map = {}
    for r in (range(h)):
      for c in (range(w)):
        value = data[r][c]
        low = True
        neighbors = []
        if (r!=0):
          # up valid
          neighbors.append(str(r-1)+','+str(c))
          low = value < data[r-1][c] and low
        if (r!=h-1):
          # down valid
          neighbors.append(str(r+1)+','+str(c))
          low = value < data[r+1][c] and low
        if (c!=0):
          # left valid
          neighbors.append(str(r)+','+str(c-1))
          low = value < data[r][c-1] and low
        if (c!=w-1):
          # right valid
          neighbors.append(str(r)+','+str(c+1))
          low = value < data[r][c+1] and low
        pos_key = str(r)+','+str(c)
        neighbors_map[pos_key] = neighbors
        value_map[pos_key] = value

        if low:
          low_points.append((str(r)+','+str(c)))

    basins = []
    for pt in low_points:
      basin = [pt]
      size = 0
      queue = [pt]
      visited = []
      while len(queue) > 0:
        print(queue)
        node = queue.pop(0)
        print('node: ', node, neighbors_map[node], value_map[node])
        visited.append(node)
        for child in neighbors_map[node]:
          print('child: ', child, neighbors_map[child], value_map[child])
          if value_map[child] > value_map[node] and value_map[child] != 9 and child not in queue and child not in visited:
            basin.append(child)
            queue += [child]
            print('new queue: ', queue)
            print('basin: ', basin)
      basins.append(basin)
    print(basins)
    sizes = [len(b) for b in sorted(basins, key=len)]

    print(sizes[-3]*sizes[-2]*sizes[-1])








        

      
        

if __name__ == "__main__":
    main(sys.argv[1:])