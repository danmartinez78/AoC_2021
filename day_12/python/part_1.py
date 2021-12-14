import sys, getopt
import numpy as np
from math import ceil
import copy

def read_input(fn):
    with open(fn) as f:
        lines = f.read().split('\n')
    return lines

def DFS(node, neighbor_map, visited, path):
  path.append(node)
  print(node, visited, path)
  if node == 'end':
    print('found path!!!!!!', path)
    return 1
  if node.islower():
    visited.append(node)
  count = 0
  for neighbor in neighbor_map[node]:
    if neighbor not in visited:
      count += DFS(neighbor, neighbor_map, copy.copy(visited), copy.copy(path))
  return count
    
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

    nodes = []
    neighbor_map = {}
    for edge in data:
      node_1, node_2 = edge.split('-')
      if node_1 not in nodes:
        nodes.append(node_1)
        neighbor_map[node_1] = []
      if node_2 not in nodes:
        nodes.append(node_2)
        neighbor_map[node_2] = []
      neighbor_map[node_1].append(node_2)
      neighbor_map[node_2].append(node_1)
    # print(nodes)
    # print(neighbor_map)      

    print(DFS('start', neighbor_map, [], []))




if __name__ == "__main__":
    main(sys.argv[1:])