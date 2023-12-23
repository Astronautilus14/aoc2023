f = [l.strip() for l in open('./day16/inp.txt').readlines()]
m = len(f)
n = len(f[0])

def next(x, y, dir):
  if dir == 0:
    return (x, y-1)
  elif dir == 1:
    return (x+1, y)
  elif dir == 2:
    return (x, y+1)
  elif dir == 3:
    return (x-1, y)

def algo(sx, sy, sdir):
  copy = [[0 for _ in range(n)] for _ in range(m)]
  seen = []
  nodes = [((sx, sy), sdir)]
  while len(nodes) > 0:
    curr, dir = nodes.pop(-1)
    while True:
      x, y = curr
      if x < 0 or x >= n or y < 0 or y >= m or (x,y,dir) in seen:
        break
      copy[y][x] = 1
      seen.append((x,y,dir))
      #print("---")
      #print("\n".join(["".join(['#' if j == 1 else '.' for j in i]) for i in copy]))
      if f[y][x] == '.':
        curr = next(x, y, dir)
      elif f[y][x] == '/':
        if dir == 0:
          dir = 1
        elif dir == 1:
          dir = 0
        elif dir == 2:
          dir = 3
        elif dir == 3:
          dir = 2
        curr = next(x, y, dir)
      elif f[y][x] == '\\':
        if dir == 0:
          dir = 3
        elif dir == 1:
          dir = 2
        elif dir == 2:
          dir = 1
        elif dir == 3:
          dir = 0
        curr = next(x, y, dir)
      elif f[y][x] == '|':
        if dir == 0 or dir == 2:
          curr = next(x, y, dir)
        else:
          dir = 0
          nodes.append((next(x, y, 2), 2))
          curr = next(x, y, dir)
      elif f[y][x] == '-':
        if dir == 1 or dir == 3:
          curr = next(x, y, dir)
        else:
          dir = 1
          nodes.append((next(x, y, 3), 3))
          curr = next(x, y, dir)

  #print("\n".join(["".join(['#' if j == 1 else '.' for j in i]) for i in copy]))

  return sum([sum(l) for l in copy])

sol = []
for i in range(n):
  sol.append(algo(i, 0, 2))
  sol.append(algo(i, m-1, 0))
  if i % 10 == 0:
    print(f"{i}/{n+m}")
for i in range(m):
  sol.append(algo(0, i, 1))
  sol.append(algo(n-1, i, 3))
  if i % 10 == 0:
    print(f"{n+i}/{n+m}")
print(max(sol))