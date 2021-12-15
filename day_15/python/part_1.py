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
    # print(data)
    h = len(data)
    w = len(data[0])
    neighbors_map = {}
    risk_map = {}
    for r in (range(h)):
      for c in (range(w)):
        value = data[r][c]
        neighbors = []
        if (r!=0):
          # up valid
          neighbors.append(str(r-1)+','+str(c))
        if (r!=h-1):
          # down valid
          neighbors.append(str(r+1)+','+str(c))
        if (c!=0):
          # left valid
          neighbors.append(str(r)+','+str(c-1))
        if (c!=w-1):
          # right valid
          neighbors.append(str(r)+','+str(c+1))
        pos_key = str(r)+','+str(c)
        neighbors_map[pos_key] = neighbors
        risk_map[pos_key] = value

    # print(risk_map)
    # print(neighbors_map)
    queue = [('0,0', 0)]
    prev = {'0,0':None}
    visited = []
    goal = str(data.shape[0] - 1) + ',' + str(data.shape[1] - 1)
    while len(queue) > 0:
      queue.sort(key = lambda x: x[1])
      node, cost = queue.pop(0)
      if node == goal:
        # back track
        print('hit goal with cost:', cost)
        break
      # print(node, cost)
      visited.append(node)
      for neighbor in neighbors_map[node]:
        if neighbor not in visited:
          neighbor_cost = cost + risk_map[neighbor]
          if neighbor in dict(queue).keys():
            pass
          else:
            queue.append((neighbor, neighbor_cost))
            prev[neighbor] = node




if __name__ == "__main__":
    main(sys.argv[1:])