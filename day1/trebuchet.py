with open("inp.txt") as f:
   sum = 0
   for line in f.readlines():
      cal = ""
      for char in line:
         if char.isdigit():
            cal += char
            break
      for char in line[::-1]:
         if char.isdigit():
            cal += char
            break
      sum += int(cal)
   print(sum)
