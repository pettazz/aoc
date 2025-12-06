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

rolling = 0
total = 0
op = ops.pop(0)
for num in numbers:
  if num == "":
    total += rolling
    if len(ops) > 0:
      op = ops.pop(0)
      rolling = 0
  else:
    if rolling == 0:
      rolling = int(num)
    else:
      rolling = op(rolling, int(num))

print(total)