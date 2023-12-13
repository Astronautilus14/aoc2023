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

print(maps)