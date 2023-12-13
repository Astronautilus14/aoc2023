# Parse input
lines = [x.rstrip() for x in open('./day5/sample.txt').readlines()]
seeds = [int(x) for x in lines.pop(0).split(': ')[1].split(' ')]
maps = []
for line in lines:
  if line == '':
    maps.append([])
  elif line.endswith(':'):
    continue
  else:
    maps[-1].append([int(x) for x in line.split(' ')])

# Part 1
def part1():
  locations = []
  for seed in seeds:
    next = seed
    for map in maps:
      for [dest_start, source_start, length] in map:
        if source_start <= next < source_start + length:
          next = dest_start + next - source_start
          break
    locations.append(next)
  print(min(locations))