import sys, getopt

def read_input(fn):
    with open(fn) as f:
        lines = f.read().splitlines()
    lines = [i.split() for i in lines]
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
    pos = [0,0,0] # horiz, depth, aim
    for command in data:
      direction = command[0]
      if direction == 'forward':
        pos[0] += int(command[1])
        pos[1] += (pos[2] * int(command[1])) 
      elif direction == 'back':
        pos[0] -= int(command[1])
      elif direction == 'up':
        pos[2] -= int(command[1])
      elif direction == 'down':
        pos[2] += int(command[1])
    
    print(pos)
    print(pos[0] * pos[1])

if __name__ == "__main__":
    main(sys.argv[1:])