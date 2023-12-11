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

# Part 2
# ranges = []
# for start, length in zip(seeds[::2], seeds[1::2]):
#   ranges.append((start, start + length - 1))
ranges = [(79, 79 + 14)]

for i, (start, end) in enumerate(ranges):
  for map in maps:
    for [dest_start, source_start, length] in map:
      dest_end = dest_start + length - 1
      source_end = source_start + length - 1

      contains_start = source_start <= start <= source_end
      contains_end = source_start <= end <= source_end

      new_start = dest_start + start - source_start
      new_end = dest_start + end - source_start

      if contains_start and contains_end:
        start, end = new_start, new_end
        ranges[i] = (new_start, new_end)
        break
      elif contains_start:
        # Split range
        new_end = dest_start + length - 1

        range_length = new_end - new_start
        ranges.append((start + range_length + 1, end))

        start, end = new_start, new_end
        ranges[i] = (new_start, new_end)
      elif contains_end:
        # Split range
        new_start = dest_start

        range_length = source_start - start
        ranges.append((start, start + range_length + 1))

        start, end = new_start, new_end
        ranges[i] = (new_start, new_end)
print(ranges)