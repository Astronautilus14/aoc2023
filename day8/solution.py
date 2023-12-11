with open("inp.txt") as file:
  lines = file.readlines()

path = lines.pop(0).strip()
nodes = {}
for [node, edges] in [line.strip().split(" = ") for line in lines[1:]]:
  nodes[node] = tuple(edges[1:-1].split(", "))

# Part 1
curr = "AAA"
steps = 0
while curr != "ZZZ":
  curr = nodes[curr][0 if path[steps % len(path)] == 'L' else 1]
  steps += 1
print(steps)

# Part 2
from math import lcm

starts = [node for node in nodes if node.endswith("A")]
loop_sizes = []
for start in starts:
  steps = 0
  curr = start
  while not curr.endswith("Z"):
    curr = nodes[curr][0 if path[steps % len(path)] == 'L' else 1]
    steps += 1
  loop_sizes.append(steps)
print(lcm(*loop_sizes))
