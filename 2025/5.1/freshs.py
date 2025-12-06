ranges = []

with open('input.txt') as f:
  rangeline = f.readline().strip()
  while rangeline != "":
    ranges.append(tuple(map(int, rangeline.split("-"))))
    rangeline = f.readline().strip()

  freshs = 0
  for itemline in f:
    item = int(itemline.strip())
    for rnge in ranges:
      if rnge[0] <= item <= rnge[1]:
        freshs += 1
        break

  print(freshs)