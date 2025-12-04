grid = []

with open('input.txt') as f:
  for line in f:
    grid.append(list(line.strip()))

moved = 0
dirs = [i for i in range(-1, 2)]

def find_movable(curgrid):
  for yidx, row in enumerate(curgrid):
    for xidx, char in enumerate(row):
      if char == '@':
        adjacents = 0
        for y in dirs:
          for x in dirs:
            checky = yidx + y
            checkx = xidx + x
            if not (checkx == xidx and checky == yidx) and \
               0 <= checky < len(curgrid) and \
               0 <= checkx < len(row) and \
               curgrid[checky][checkx] == "@":
              adjacents += 1
        if adjacents < 4:
          return (yidx, xidx)

  return False

movedpos = find_movable(grid)
while movedpos:
  grid[movedpos[0]][movedpos[1]] = 'x'
  moved += 1
  movedpos = find_movable(grid)

print("moved:", moved)
