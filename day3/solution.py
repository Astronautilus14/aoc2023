# Part 1
with open("sample.txt") as f:
  grid = [ [ (None if char == '.' else char, False) for char in line.strip() ] for line in f.readlines() ]
  sum = 0
  for i, line in enumerate(grid):
    for j, [char, visted] in enumerate(line):
      if char and not char.isdigit():
        neigbours = [(k, m) for k in range(i-1, i+2) if k >= 0 and k < len(grid) for m in range(j-1, j+2) if m >= 0 and m < len(line) and grid[k][m][0] and grid[k][m][0].isdigit()]
        for [y, x] in neigbours:
          [neigbours, visited] = grid[y][x]
          if neigbours and neigbours.isdigit() and not visited:
            k = 0
            while x - k > 0 and grid[y][x-k-1][0] and grid[y][x-k-1][0].isdigit():
              k += 1

            digits = ""
            l = 0
            while x-k+l < len(line):
              [next, _] = grid[y][x-k+l]
              if next and next.isdigit():
                digits += next
                grid[y][x-k+l] = (next, True)
                l += 1
              else:
                break

            sum += int(digits)
  print(sum)

# Part 2
with open("inp.txt") as f:
  grid = [ [ (None if char == '.' else char, False) for char in line.strip() ] for line in f.readlines() ]
  sum = 0
  for i, line in enumerate(grid):
    for j, [char, visted] in enumerate(line):
      if char == '*':
        neigbours = [(k, m) for k in range(i-1, i+2) if k >= 0 and k < len(grid) for m in range(j-1, j+2) if m >= 0 and m < len(line) and grid[k][m][0] and grid[k][m][0].isdigit()]
        numbers = []
        for [y, x] in neigbours:
          [neigbours, visited] = grid[y][x]
          if neigbours and neigbours.isdigit() and not visited:
            k = 0
            while x - k > 0 and grid[y][x-k-1][0] and grid[y][x-k-1][0].isdigit():
              k += 1

            digits = ""
            l = 0
            while x-k+l < len(line):
              [next, _] = grid[y][x-k+l]
              if next and next.isdigit():
                digits += next
                grid[y][x-k+l] = (next, True)
                l += 1
              else:
                break

            numbers.append(int(digits))
        if len(numbers) == 2:
          sum += numbers[0] * numbers[1]
  print(sum)