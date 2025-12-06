with open('input.txt') as f:
  ranges = []
  for line in f:
    if line.strip() == "":
      # we don't need the rest anymore
      break
    ranges.append(tuple(map(int, line.split("-"))))
  ranges = sorted(ranges)

  total = 0
  currmin = -1

  for (start, end) in ranges:
    if currmin >= start:
      start = currmin + 1

    if start <= end:
      total += end - start + 1

    if end > currmin:
      currmin = end

  print(total)