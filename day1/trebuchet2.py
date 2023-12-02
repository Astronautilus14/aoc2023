digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def findChar(line, reverse=False):
   for i, char in enumerate(line):
      if char.isdigit():
         return char
      for j, digit in enumerate(digits):
         d = digit[::-1] if reverse else digit
         if line[i:].startswith(d):
            return str(j+1)

with open("inp.txt") as f:
   sum = 0
   for line in f.readlines():
      sum += int(findChar(line) + findChar(line[::-1], True))
   print(sum)
