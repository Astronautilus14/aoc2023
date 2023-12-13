with open('./day13/inp.txt') as f:
    grids = [l.splitlines() for l in f.read().split("\n\n")]

def check_horizontal_reflaction(grid):
  for i in range(1, len(grid)):
    for r1, r2 in zip(grid[:i][i-len(grid):], grid[i:i*2][::-1]):
      if r1 != r2:
        break
    else:
      return i
  return 0

def check_horizontal_reflaction_with_smudge(grid):
  for i in range(1, len(grid)):
    smudge = False
    for r1, r2 in zip(grid[:i][i-len(grid):], grid[i:i*2][::-1]):
      if r1 == r2:
        continue
      if smudge:
        break

      # Check if r1 and r2 differ by only one character
      found_one = False
      for char1, char2 in zip(r1, r2):
        if char1 != char2:
          if found_one:
            break
          found_one = True
      else:
        smudge = True
      if not smudge:
        break
    else:
      if smudge:
        return i
  return 0

acc = 0
for grid in grids:
  acc += 100 * check_horizontal_reflaction_with_smudge(grid)
  acc += check_horizontal_reflaction_with_smudge(list(zip(*grid[::-1])))

print(acc)


