import time

# Part 1
f = open('sample.txt').read().split('\n')
f = list(zip(*f[::-1]))
acc = 0
for l in f:
  idx  = 0
  for i,t in enumerate(l[::-1]):
    if t == '#':
      idx = i+1
    if t == 'O':
      acc += len(l) - idx
      idx += 1
print(acc)

# Part 2
# 90 deg clockwise rotation
def rotate(g):
  return list(zip(*g[::-1]))

cache = {}
def tilt_cache(g, d):
  fg = tuple(g) 
  if (fg, d) in cache:
    return cache[(fg, d)], True
  res = tilt(g, d)
  cache[(fg, d)] = res
  return res, False


def tilt(g, d):
  g = list(g)
  for _ in range(d):
    g = rotate(g)

  ng = []
  for l in g:
    idx  = 0
    nl = ['.']*len(l)
    for i,t in enumerate(l[::-1]):
      if t == '#':
        nl[len(l)-i-1] = '#'
        idx = i+1
      elif t == 'O':
        nl[len(l)-idx-1] = 'O'
        idx += 1
    ng.append(nl)

  for _ in range(4-d):
    ng = rotate(ng)
  
  return tuple(ng)

f = tuple(open('inp.txt').read().split('\n'))
d ={
  0: 1,
  1: 2,
  2: 3,
  3: 0
}

def print_grid(g, m=""):
  print(m)
  print("\n".join(["".join(x) for x in g]))
  print("---")

cycles = 1000000000
# 1 N, 0 E, 3 S, 2 W
def part2(f):
  cycle_start = None
  cycle_start_idx = -1
  cycle_start_dir = -1
  # print("\n".join(["".join(x) for x in f]))
  # print("---")
  for i in range(cycles):
    # print(f"After {i} cycles:")
    # print("\n".join(["".join(x) for x in f]))
    # print("---")
    for j in range(4):
      f, from_cache = tilt_cache(f, d[j])
      # print("\n".join(["".join(x) for x in f]))
      # print("---")
      if from_cache and cycle_start is None:
        cycle_start = (f,j)
        cycle_start_idx = i
        cycle_start_dir = j
      elif cycle_start is not None and cycle_start[0] == f and cycle_start[1] == j:
        #print(i)
        l = i - cycle_start_idx
        return cycle_start_idx-l+1, cycle_start_dir, l, cycle_start

start, dir, length, (cycle, _) = part2(f)
#print(f"Start: {start}, dir: {dir}, length: {length}")
# Do remaining directions
for i in range(dir+1, 4):
  cycle, _ = tilt_cache(cycle, d[i])

# Do remaining cycles
for i in range((cycles-start)%length):
  for j in range(4):
    cycle, _ = tilt_cache(cycle, d[j])

print_grid(cycle, "Final")
# Calculate ans
acc = 0
for i, l in enumerate(cycle):
  acc += l.count('O') * (len(cycle) - i)
print(acc)