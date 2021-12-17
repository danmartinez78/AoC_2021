import sys, getopt
import numpy as np
from math import ceil, floor, sqrt
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
        # lines = [list(l) for l in lines]
        # lines = [list(map(int, n)) for n in lines]
    return lines[0]

def step(pos, vel):
  pos[0] += vel[0]
  pos[1] += vel[1]
  if vel[0] < 0:
    vel += 1
  elif vel[0] > 0:
    vel[0] -= 1
  vel[1] -= 1
  return pos, vel

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
    data = data.split(': ')[1]
    x, y = data.split(',')
    x_min, x_max = x.split('=')[1].split('..')
    y_min, y_max = y.split('=')[1].split('..')
    x_target = list(range(int(x_min), int(x_max) + 1))
    y_target = list(range(int(y_min), int(y_max) + 1))

    # print(x_target, y_target)
    for i in range(min(x_target)):
      sum = 0
      for j in range(i,-1,-1):
        sum += j
      if sum > min(x_target):
        print(i)
        min_vx = i
        break
    max_vx = max(x_target) + 1
    print(min_vx, max_vx)
    count = 0
    vels = []
    for vx in range(min_vx, max_vx):
      for vy in range(min(y_target), 1000):
        pos = [0,0]
        v = [vx, vy]
        max_h = 0
        for i in range(5000):
          pos, v = step(pos, v)
          if pos[1] > max_h:
            max_h = pos[1]
          # print(pos, v)
          if pos[0] in x_target and pos[1] in y_target:
            print('hit target!!!!')
            count += 1
            vels.append([vx, vy])
            break
          if v[0] == 0 and pos[1] < min(y_target) or pos[0] > max(x_target):
            break
    print(count)
    # print(vels)
    
if __name__ == "__main__":
    main(sys.argv[1:])