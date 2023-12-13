def create_arrangements(line, size):
  c = line.count('?')
  hashtag_count = line.count('#')
  res = []
  for i in range(2**c):
    bit_map = bin(i)[2:].zfill(c)
    if bit_map.count('1') + hashtag_count != size:
      continue
    unkown_counter = 0
    arrangement = ''
    for char in line:
      if char == '?':
        arrangement += ('#' if bit_map[unkown_counter] == '1' else '.')
        unkown_counter += 1
      else:
        arrangement += char
    res.append(arrangement)
  return res

def create_groups(arrangement):
  groups = []
  c = 0
  for char in arrangement+'.':
    if char == '#':
      c += 1
    elif c > 0:
      groups.append(c)
      c = 0
  return groups

lines = [(l, list(map(int, rules.split(",")))) for [l, rules] in [l.strip().split(" ") for l in open('inp.txt')]]

acc = 0
for i, (line, rules) in enumerate(lines):
  print(line, rules)
  print(f"Line {i+1}/{len(lines)}")
  arrangements = create_arrangements(line, sum(rules))
  for arrangement in arrangements:
    groups = create_groups(arrangement)
    if groups == rules:
      acc += 1
print(acc)