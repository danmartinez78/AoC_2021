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
    print(data)
    data = data.split(': ')[1]
    x, y = data.split(',')
    x_min, x_max = x.split('=')[1].split('..')
    y_min, y_max = y.split('=')[1].split('..')
    x_target = list(range(int(x_min), int(x_max) + 1))
    y_target = list(range(int(y_min), int(y_max) + 1))

    print(x_target, y_target)

    

    max_dx = int(x_max)

    # vf^2 = vo^2 + 2 * a * d -> vo = sqrt(2ad)
    min_vx = floor(sqrt(1.5*max_dx))
    max_vx = ceil(sqrt(max_dx)) + 10
    print(min_vx, max_vx)
    heights = []
    for vx in range(min_vx, max_vx):
      for vy in range(10000):
        pos = [0,0]
        v = [vx, vy]
        max_h = 0
        for i in range(1000):
          pos, v = step(pos, v)
          if pos[1] > max_h:
            max_h = pos[1]
          # print(pos, v)
          if pos[0] in x_target and pos[1] in y_target:
            print('hit target!!!!', vx, vy, max_h)
            heights.append(max_h)
          if pos[0] > max(x_target) and pos[1] > max(y_target):
            break
    print(max(heights))
    

    

if __name__ == "__main__":
    main(sys.argv[1:])