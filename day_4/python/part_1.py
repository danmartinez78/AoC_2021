import sys, getopt
import numpy as np
from math import ceil
import copy

class Board:
  def __init__(self, numbers):
    self.numbers = np.asarray(numbers).reshape((5,5))
    self.marks = np.zeros(shape = (5,5))
    self.winning_num = 0
  
  def play_turn(self, num):
    index = np.where(self.numbers == num)
    self.marks[index] = 1

  def check_win(self, num):
    # calc sums
    row_sum = np.sum(self.marks, axis = 0)
    col_sum = np.sum(self.marks, axis = 1)
    # print('sums', row_sum, col_sum)
    # check for win
    if np.max(row_sum) == 5 or np.max(col_sum) == 5:
      self.winning_num = int(num)
      return True
    else:
      return False

  def calc_score(self):
    indices = np.where(self.marks == 0)
    sum = np.sum(self.numbers.astype(int)[np.where(self.marks == 0)])
    return sum*self.winning_num

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n\n')
        lines = [l.split() for l in lines]
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
    nums = data[0][0].split(',')
    print(nums)
    boards = []
    for vals in data[1:]:
      boards.append(Board(vals))
    
    game_over = False
    for num in nums:
      if (game_over):
        break
      for b in boards:
        # print("BOARD Before:")
        # print(b.numbers, '\n', b.marks)
        # print('number', num)
        b.play_turn(num)
        # print("BOARD After:")
        # print(b.numbers, '\n', b.marks)
        if (b.check_win(num)):
          print('WIN!!!!!')
          game_over = True
          print(b.numbers, '\n', b.marks)
          print(b.calc_score())
          break

if __name__ == "__main__":
    main(sys.argv[1:])