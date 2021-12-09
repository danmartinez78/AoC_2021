import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
        lines = [n.split(' | ') for n in lines]
        # lines = [l.replace(" ", "") for l in lines]
        
    return lines

def contains(s1, s2):
    return len(list(set(s1)&set(s2)))

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
    
    sum = 0
    for line in data:
      sequence = line[0].split(' ')
      output = line[1].split(' ')
      sequence = sorted(sequence, key=len)
      print(sequence, ' | ', output)
      cypher = [""]*10
      for digit in sequence:
        count = len(digit)
        if count == 2:
          cypher[1] = digit
        elif count == 3:
          cypher[7] = digit
        elif count == 4:
          cypher[4] = digit
        elif count == 7:
          cypher[8] = digit
        elif count == 5:
          if contains(digit, cypher[1]) == 2:
            cypher[3] = digit
          elif contains(digit, cypher[4]) == 3:
            cypher[5] = digit
          else:
            cypher[2] = digit
        elif count == 6:
          if contains(digit, cypher[1]) == 1:
            cypher[6] = digit
          elif contains(digit, cypher[4]) == 4:
            cypher[9] = digit
          else:
            cypher[0] = digit
      print(cypher)
      num = ''
      for digit in output:
        tests = [contains(digit, x) == len(digit) and len(x) == len(digit) for x in cypher]
        for i in range(len(tests)):
          if tests[i]:
            num += str(i)
      print(num)
      sum+=int(num)
    print(sum)

      
   

if __name__ == "__main__":
    main(sys.argv[1:])