lines = [
  list(map(int, x.strip().split(" "))) for x in open("inp.txt").readlines()
]

# Part 1
acc = 0
for line in lines:
  diffs = [line]
  while any(x != 0 for x in diffs[-1]):
    diffs.append([y - x for x, y in zip(diffs[-1], diffs[-1][1:])])

  curr = 0
  for diff in diffs[len(diffs) - 2::-1]:
    curr += diff[-1]
  acc += curr
print(acc)

# Part 2
acc = 0
for line in lines:
  diffs = [line]
  while any(x != 0 for x in diffs[-1]):
    diffs.append([y - x for x, y in zip(diffs[-1], diffs[-1][1:])])

  curr = 0
  for diff in diffs[len(diffs) - 2::-1]:
    curr = -curr + diff[0]
  acc += curr
print(acc)
