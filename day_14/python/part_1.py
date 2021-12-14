import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n\n')
        template = lines[0]
        rules = lines[1].split('\n')
    return template, rules
   
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
    
    template, rules = read_input("../inputs/" + inputfile)
    print(template, rules)
    insertion_map = {}
    for rule in rules:
      key, insertion = rule.split(' -> ')
      insertion_map[key] = insertion
    print(insertion_map)
    
    steps = 10
    poly = template
    for i in range(steps):
      new_poly = ''
      for j in range(len(poly)-1):
        # print(poly[j:j+2])
        new_poly += poly[j] + insertion_map[poly[j:j+2]]
      poly = new_poly + poly[-1]
      print(i)
    letters = set(list(poly))
    counts = []
    for letter in letters:
      counts.append(poly.count(letter))
    print(max(counts)- min(counts))
    

    










if __name__ == "__main__":
    main(sys.argv[1:])