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
    h = len(data)
    w = len(data[0])
    neighbors_map = {}
    energy_map = {}
    octipodes = []
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
        if (c!=w-1 and r!=0):
          # right up valid
          neighbors.append(str(r-1)+','+str(c+1))
        if (c!=w-1 and r!=h-1):
          # right down valid
          neighbors.append(str(r+1)+','+str(c+1))
        if (c!=0 and r!=0):
          # left up valid
          neighbors.append(str(r-1)+','+str(c-1))
        if (c!=0 and r!=h-1):
          # left down valid
          neighbors.append(str(r+1)+','+str(c-1))
        
        pos_key = str(r)+','+str(c)
        octipodes.append(pos_key)
        neighbors_map[pos_key] = neighbors
        energy_map[pos_key] = value

    # print(energy_map)
    # print(neighbors_map)

    flashes = 0
    simultaneous_flashes = []
    for i in range(500):
      flashers = []
      for oct in octipodes:
        energy_map[oct] += 1
        if energy_map[oct] > 9:
          flashers.append(oct)
      flashed = []
      while (len(flashers)>0):
        flasher = flashers.pop(0)
        flashes += 1
        if flasher not in flashed:
          flashed.append(flasher)
          # augment neighbors
          for adj in neighbors_map[flasher]:
            energy_map[adj] += 1
            if energy_map[adj] > 9 and adj not in flashed and adj not in flashers:
              flashers.append(adj)
        for spent in flashed:
          energy_map[spent] = 0
        if set(flashed) == set(octipodes):
          simultaneous_flashes.append(i+1)
    print(flashes)
    print(simultaneous_flashes)    

if __name__ == "__main__":
    main(sys.argv[1:])