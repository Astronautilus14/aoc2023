# Part 1
# races = [(7, 9), (15, 40), (30, 200)]

# Part 2
races = [(41968894, 214178911271055)]

res = 1
for t, d in races:
  c = 0
  for button_hold in range(1, t):
    if button_hold * (t - button_hold) > d:
      c += 1
  res *= c
print(res)