from math import ceil

lines = [l.strip() for l in open('./day10/inp.txt').readlines()]

north_pipes = '|7FS'
south_pipes = '|JLS'
east_pipes = '-J7S'
west_pipes = '-FLS'

# Part 1
def find_start():
  for y, line in enumerate(lines):
    for x, c in enumerate(line):
      if c == 'S':
        return x, y
  raise Exception("No start found")

def get_neighbor(x, y, direction='nsew'):
  # North
  if 'n' in direction and y > 0 and lines[y-1][x] in north_pipes:
    return x, y-1, 'nwe_'[north_pipes.index(lines[y-1][x])]

  # South
  if 's' in direction and y < len(lines) - 1 and lines[y+1][x] in south_pipes:
    return x, y+1, 'swe_'[south_pipes.index(lines[y+1][x])]

  # East
  if 'e' in direction and x < len(lines[y]) - 1 and lines[y][x+1] in east_pipes:
    return x+1, y, 'ens_'[east_pipes.index(lines[y][x+1])]

  # West
  if 'w' in direction and x > 0 and lines[y][x-1] in west_pipes:
    return x-1, y, 'wsn_s'[west_pipes.index(lines[y][x-1])]
  
  raise Exception(f"No neighbor found for {x}, {y}, {direction}")

      
start_x, start_y = find_start()
x, y, dir = get_neighbor(start_x, start_y)
length = 1
while not (x == start_x and y == start_y):
  x, y, dir = get_neighbor(x, y, dir)
  length += 1
print(ceil(length / 2))