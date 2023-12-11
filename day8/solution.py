lines = open("sample.txt ").readlines()
path = lines.pop(0)
lines = [ line.strip() for line in lines[1:] ]

print(lines)