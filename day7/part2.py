lines = [line.strip().split(" ") for line in open('inp.txt')]

J = 'J'

# Part 2
def check_same_kind(cards, n, return_char=False, joker=True):
  jokers = cards.count(J) if joker else 0
  if jokers == n:
    if return_char:
      return J
    return True
  
  for char in cards:
    if char == J and joker:
      continue
    if joker and cards.count(char) + jokers >= n or cards.count(char) == n:
      if return_char:
        return char
      return True
  return False

def check_full_house(cards):
  return check_two_pair(cards, joker=False) and cards.count(J) == 1 or check_same_kind(cards, 3, joker=False) and check_same_kind(cards, 2, joker=False)

def check_two_pair(cards, joker=True):
  first = check_same_kind(cards, 2, True, False)
  if not first:
    return False
  return check_same_kind([c for c in cards if c != first], 2, joker=joker)

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
pair = []
high_card = []

for line in lines:
  if check_same_kind(line[0], 5):
    five_of_a_kind.append(line)
    continue

  if check_same_kind(line[0], 4):
    four_of_a_kind.append(line)
    continue

  if check_full_house(line[0]):
    full_house.append(line)
    continue

  if check_same_kind(line[0], 3):
    three_of_a_kind.append(line)
    continue

  if check_two_pair(line[0]):
    two_pair.append(line)
    continue

  if check_same_kind(line[0], 2):
    pair.append(line)
    continue

  high_card.append(line)

card_order = "AKQT98765432J"

def getValues(card):
  return [card_order.index(char) for char in card[0]]

five_of_a_kind.sort(key=getValues)
four_of_a_kind.sort(key=getValues)
full_house.sort(key=getValues)
three_of_a_kind.sort(key=getValues)
two_pair.sort(key=getValues)
pair.sort(key=getValues)
high_card.sort(key=getValues)

ordered = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + pair + high_card

# print("Five of a kind", five_of_a_kind)
# print("Four of a kind", four_of_a_kind)
# print("Full house", full_house)
# print("Three of a kind", three_of_a_kind)
# print("Two pair", two_pair)
# print("Pair", pair)
# print("High card", high_card)

res = 0
for i, [_, bid] in enumerate(ordered[::-1]):
  res += int(bid) * (i+1)
print(res)