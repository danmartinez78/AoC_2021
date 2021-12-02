import sys, getopt

def read_input(fn):
    with open(fn) as f:
        lines = f.read().splitlines()
    lines = [int(i) for i in lines]
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

    data = read_input(inputfile)
    print(data)

    inc = 0
    for i in range(0, len(data)-2):
      a = sum(data[i:i+3])
      b = sum(data[i+1:i+4])
      if b > a:
        inc += 1
    print(inc)



if __name__ == "__main__":
    main(sys.argv[1:])