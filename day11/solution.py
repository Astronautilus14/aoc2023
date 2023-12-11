grid = [l.strip() for l in open('inp.txt')]

# Part 1
def expand(grid):
  expanded = []
  for row in grid:
    expanded.append(row)
    if not any([c=='#' for c in row]):
      expanded.append(row)
  return expanded

expanded = expand(list(zip(*(expand(grid))[::-1])))

galaxies = []
for y, row in enumerate(expanded):
  for x, cell in enumerate(row):
    if cell == '#':
      galaxies.append((x, y))

acc = 0
for i, (x1, y1) in enumerate(galaxies):
  for x2, y2 in galaxies[i:]:
    acc += abs(x1-x2) + abs(y1-y2)
print(acc)

# Part 2
def expand1m(grid):
  expanded = []
  for row in grid:
    if not any([c=='#' for c in row]):
      expanded.append(['X']*len(row))
    else:
      expanded.append(row)
  return expanded

expanded = expand1m(list(zip(*(expand1m(grid))[::-1])))

galaxies = []
for y, row in enumerate(expanded):
  for x, cell in enumerate(row):
    if cell == '#':
      galaxies.append((x, y))

size = 999999
acc = 0
for i, (x1, y1) in enumerate(galaxies):
  for x2, y2 in galaxies[i:]:
    acc += abs(y1-y2)
    for i in range(min(y1,y2), max(y1,y2)+1):
      if expanded[i][x1] == 'X':
        acc += size

    acc += abs(x1-x2)
    for i in range(min(x1,x2), max(x1,x2)+1):
      if expanded[y1][i] == 'X':
        acc += size
print(acc)
