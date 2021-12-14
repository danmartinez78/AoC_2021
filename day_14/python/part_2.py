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
    letter_count = {}
    letter_map = {}
    for rule in rules:
      key, insertion = rule.split(' -> ')
      letter_map[key] = insertion
      if insertion not in letter_count.keys():
        letter_count[insertion] = 0
      insertion_map[key] = list((key[0] + insertion, insertion + key[1]))
    print(insertion_map)

    counts = {}
    for key in insertion_map.keys():
      counts[key] = 0

    for j in range(len(template)-1):
      counts[template[j]+template[j+1]] += 1
      letter_count[template[j]] += 1
    letter_count[template[-1]] += 1
    
    steps = 40
    for i in range(1,steps+1):
      print('step', i)
      frozen_counts = copy.deepcopy(counts)
      for symbol in frozen_counts.keys():
        if frozen_counts[symbol] > 0:
          counts[symbol] -= frozen_counts[symbol]
          letter_count[letter_map[symbol]] += frozen_counts[symbol]
          for child in insertion_map[symbol]:
            print(frozen_counts[symbol], symbol, ' yields ', frozen_counts[symbol], child)
            counts[child] += frozen_counts[symbol]
      
      # print(counts)
      print(letter_count)
      least = min(letter_count.values())
      most = max(letter_count.values())
      print(most - least)

if __name__ == "__main__":
    main(sys.argv[1:])