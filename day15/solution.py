f = open('inp.txt').readline().split(',')

def my_hash(i):
  curr = 0
  for l in i:
    curr += ord(l)
    curr *= 17
    curr %= 256
  return curr

# Part 1
acc = 0
for i in f:
  acc += my_hash(i)
print(acc)

def debug(boxes, operation):
  print(f"\nAfter \"{operation}\":")
  filtered = []
  for i, box in enumerate(boxes):
    if i in used_idx:
      filtered.append(box)
  boxes = new
  for i, box in enumerate(filtered):
    arr = []
    for label, focal in box:
      arr.append(f"[{label} {focal}]")
    print(f"Box {i}: {' '.join(arr)}")

# Part 2
boxes = [[]]*256
used_idx = []
for i in f:
  if i.endswith('-'):
    box = my_hash(i[:-1])
    new = []
    for label, focal in boxes[box]:
      if label != i[:-1]:
        new.append((label, focal))
    boxes[box] = new
  else:
    [new_label, new_focal] = i.split('=')
    box = my_hash(new_label)
    new = []
    found = False
    for label, focal in boxes[box]:
      if label == new_label:
        new.append((label, new_focal))
        found = True
      else:
        new.append((label, focal))
    if not found:
      new.append((new_label, new_focal))
    boxes[box] = new
  used_idx.append(box)
  #debug(boxes, i)

# new = []
# for i, box in enumerate(boxes):
#   if i in used_idx:
#     new.append(box)
# boxes = new

acc = 0
for i, box in enumerate(boxes):
  for j, (label, focal) in enumerate(box):
    print(label, i+1, j+1, focal)
    acc += (i+1) * (j+1) * int(focal)
print(acc)