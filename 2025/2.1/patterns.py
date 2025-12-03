def counter(start, end):
  matches = [0]

  if len(end) < 2:
    return matches

  for li in range(int(start[:len(start)//2]), int(end[:len(end)//2]) + 1):
    testnum = int(str(li) + str(li))
    if int(start) <= testnum <= int(end):
      matches.append(testnum)

  return matches

total = 0

with open('test.txt') as f:
  for idstr in f.readline().strip().split(','):
    idrange = [str(int(i)) for i in idstr.split('-')]

    # if both sides have odd number of digits, no possibilities
    if len(idrange[0]) % 2 > 0 and len(idrange[1]) % 2 > 0:
      continue

    # if start has odd digits, round up to the next even digit number
    if len(idrange[0]) % 2 > 0:
      idrange[0] = str(10 ** (len(idrange[1]) - 1))

    # if end has odd digits, round down to the nearest even digit number
    if len(idrange[1]) % 2 > 0:
      idrange[1] = str(10 ** (len(idrange[1]) - 1) - 1)

    total += sum(counter(idrange[0], idrange[1]))

print(total)