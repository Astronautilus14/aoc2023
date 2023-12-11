# Part 1
races = [(7, 9), (15, 40), (30, 200)]

# Part 2
# races = [(41968894, 214178911271055)]

# Solution
res = 1
for t, d in races:
  c = 0
  for button_hold in range(1, t):
    if button_hold * (t - button_hold) > d:
      c += 1
  res *= c
print(res)

# Part 2 opitimized
import math
t = 41968894
d = 214178911271055

# x * (t - x) = d
# xt - x^2 = d
# -x^2 + tx - d = 0
# x^2 - tx + d = 0
# x = (t +- sqrt(t^2 - 4d)) / 2

upper = math.ceil((t + (t**2 - 4*d)**0.5) / 2)
lower = math.floor((t - (t**2 - 4*d)**0.5) / 2)
print(upper - lower - 1)
