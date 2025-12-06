from functools import reduce
from operator import mul, add

numbers = None
ops = None
with open('input.txt') as f:
  for row in f:
    if "+" in row or "*" in row.strip():
      ops = [mul if op == "*" else add for op in row.split()]
      break
    if numbers is None:
      numbers = [""] * len(row)
    for idx, char in enumerate(row):
      if char not in [" ", "\n"]:
        numbers[idx] += char

numgroups = []
rolling = [ops.pop(0)]
for num in numbers:
  if num != "":
    rolling.append(int(num))
  else:
    numgroups.append(rolling)
    if len(ops) > 0:
      rolling = [ops.pop(0)]

total = 0
for group in numgroups:
  total += reduce(group[0], group[1:])

print(total)
