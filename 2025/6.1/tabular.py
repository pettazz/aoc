from functools import reduce
from operator import mul, add

maths = []
ops = []

with open('input.txt') as f:
  for line in f:
    row = line.strip().split()
    if row[0] != "" and row[0] not in ["+", "*"]:
      maths.append([int(i) for i in row])
    else:
      ops = [mul if op == "*" else add for op in row]

totals = [0] * len(ops)
for idx, op in enumerate(ops):
  totals[idx] =+ reduce(op, [row[idx] for row in maths])

print(sum(totals))
