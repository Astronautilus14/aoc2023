# Parse input
cards = [ [ list(map(int, filter(lambda x: x != '', side.split(" ")))) for side in line.rstrip().split(": ")[1].split(" | ") ] for line in open('inp.txt').readlines()]

# Part 1
acc = 0
for [winning, own] in cards:
  count = 0
  for num in winning:
    if num in own:
      count += 1
  if count > 0:
    acc += 2**(count-1)
print(acc)

# Part 2
card_count = [1]*len(cards)
for i, [winning, own] in enumerate(cards):
  count = 0
  for num in winning:
    if num in own:
      count += 1
      card_count[i+count] += card_count[i]
print(sum(card_count))