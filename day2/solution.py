max = {
   "red": 12,
   "green": 13,
   "blue": 14
}
# Part 1
with open("sample1.txt") as f:
   sum = 0
   for line in f.readlines():
      [game, rounds] = line.rstrip("\n").split(":")
      # sums = {"red": 0, "green": 0, "blue": 0}
      for round in rounds.split(";"):
         for set in round.split(","):
            [amount, colour] = set.split(" ")[1:]
            if int(amount) > max[colour]:
               break
         else:
            continue
         break
            # sums[colour] += int(amount)
      # for colour in sums.keys():
         # if sums[colour] > max[colour]:
            # break
      else:
         [_, id] = game.split(" ")
         sum += int(id)
   print(sum)

# Part 2
with open("inp.txt") as f:
   sum = 0
   for line in f.readlines():
      [game, rounds] = line.rstrip("\n").split(":")
      maxes = {"red": 0, "green": 0, "blue": 0}
      for round in rounds.split(";"):
         for set in round.split(","):
            [amount, colour] = set.split(" ")[1:]
            if int(amount) > maxes[colour]:
               maxes[colour] = int(amount)
      power = maxes["red"] * maxes["green"] * maxes["blue"]
      sum += power
   print(sum)
