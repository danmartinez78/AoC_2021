import sys
import getopt
import numpy as np
import copy
from math import ceil

def read_input(fn):
    with open(fn) as f:
        lines = f.read().splitlines()
    return lines


def find_most_least_common(data):
  gamma = ''
  epsilon = ''
  data = np.asarray(data)
  counts = np.zeros(len(data[0]))
  for bits in data:
      for i in range(len(data[0])):
        if bits[i] == '1':
          counts[i] += 1
  for i in range(len(counts)):
    if counts[i] >= ceil(len(data)/2):
      gamma +=  '1'
      epsilon += '0'
    else:
      gamma +=  '0'
      epsilon += '1'
  return gamma, epsilon


def oxygen(data):
  for i in range(len(data[0])):
    if len(data) <= 1:
      break
    most, least = find_most_least_common(data)
    bit = most[i]
    print(bit, data)
    for cand in data[:]:
      if cand[i] != bit:
        data.remove(cand)
  return data[0]

def co2(data):
  for i in range(len(data[0])):
    if len(data) <= 1:
      break
    most, least = find_most_least_common(data)
    bit = least[i]
    print(bit, data)
    for cand in data[:]:
      if cand[i] != bit:
        data.remove(cand)
  return data[0]
    

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
    ogr = int(oxygen(copy.copy(data)),2)
    csr = int(co2(copy.copy(data)),2)
    print(ogr, csr, ogr*csr)

if __name__ == "__main__":
    main(sys.argv[1:])