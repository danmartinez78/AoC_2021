import sys, getopt
import numpy as np

def read_input(fn):
    with open(fn) as f:
        lines = f.read().splitlines()
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
    print(data)
    data = np.asarray(data)
    print(data)
    gamma = ''
    epsilon = ''
    counts = np.zeros(len(data[0]))
    for bits in data:
      print(bits)
      for i in range(len(data[0])):
        if bits[i] == '1':
          counts[i] += 1
    for i in range(len(counts)):
      if counts[i] > int(len(data)/2):
        gamma +=  '1'
        epsilon += '0'
      else:
        gamma +=  '0'
        epsilon += '1'
    print(gamma, epsilon)
    print(int(gamma, 2) * int(epsilon, 2))



if __name__ == "__main__":
    main(sys.argv[1:])