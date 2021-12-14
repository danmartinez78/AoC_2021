import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n\n')
        dots = lines[0].split('\n')
        folds = lines[1].split('\n')
        folds = [f.split(' ')[-1] for f in folds]
    return dots, folds

def display_dots(dots):
      np.set_printoptions(threshold=np.inf)
      x_values = [int(dot.split(',')[0]) for dot in dots]
      y_values = [int(dot.split(',')[1]) for dot in dots]
      w = max(x_values) + 1
      h = max(y_values) + 1
      dot_matrix = np.zeros((w,h), dtype='U10')
      dot_matrix[:] = '.'
      for r,c in zip(x_values, y_values):
        dot_matrix[r][c] = '*'
      print(dot_matrix)

    
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
    
    dots, folds= read_input("../inputs/" + inputfile)
    print(dots)
    print(folds)
    visible = []
    for fold in folds:
      axis, index = fold.split('=')
      index = int(index)
      if axis == 'y':
        # modify y values
        for dot in dots[:]:
          x,y = dot.split(',')
          y = int(y)
          if y == index:
            dots.remove(dot)
          elif y > index:
            dots.remove(dot)
            new_y = str(y - ((y-index)*2))
            new_dot = x + ',' + new_y
            if new_dot not in dots:
              dots.append(new_dot)
      if axis == 'x':
        # modify x values
        for dot in dots[:]:
          x,y = dot.split(',')
          x = int(x)
          if x == index:
            dots.remove(dot)
          elif x > index:
            dots.remove(dot)
            new_x = str(x - ((x-index)*2))
            new_dot = new_x + ',' + y
            if new_dot not in dots:
              dots.append(new_dot)
      display_dots(dots)
      visible.append(len(dots))
    # sorted_dots = sorted(dots, key=lambda x: int(x[0]))
    print(visible)
            
            










if __name__ == "__main__":
    main(sys.argv[1:])