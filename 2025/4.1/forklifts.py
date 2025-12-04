grid = []

with open('input.txt') as f:
  for line in f:
    grid.append(list(line.strip()))

spots = 0
dirs = [i for i in range(-1, 2)]

for yidx, row in enumerate(grid):
  for xidx, char in enumerate(row):
    if char == '@':
      adjacents = 0
      for y in dirs:
        for x in dirs:
          checky = yidx + y
          checkx = xidx + x
          if not (checkx == xidx and checky == yidx) and \
             0 <= checky < len(grid) and \
             0 <= checkx < len(row) and \
             grid[checky][checkx] == "@":
            adjacents += 1
      if adjacents < 4:
        spots += 1

print("spots:", spots)
