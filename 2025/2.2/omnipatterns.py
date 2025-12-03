def dumbfactorize(num):
  # this is only sane because we know input won't have any wildly large numbers
  return [i for i in range(2, num + 1) if num % i == 0]

def counter(tuprange):
  matches = set([0])
  start = tuprange[0]
  end = tuprange[1]

  if len(end) < 2:
    return sum(matches)

  factors = dumbfactorize(len(start))
  for factor in factors:
    for li in range(int(start[:len(start)//factor]), int(end[:len(end)//factor]) + 1):
      testnum = int(str(li) * factor)
      if int(start) <= testnum <= int(end):
        matches.add(testnum)

  return sum(matches)

ranges = []

with open('input.txt') as f:
  for idstr in f.readline().strip().split(','):
    idrange = [str(int(i)) for i in idstr.split('-')]

    # if each side has a different number of digits, split it into two ranges
    if len(idrange[0]) != len(idrange[1]):
      ranges.append((idrange[0], str(10 ** (len(idrange[1]) - 1) - 1)))
      ranges.append((str(10 ** (len(idrange[1]) - 1)), idrange[1]))
    else:
      ranges.append(idrange)

print(sum(map(counter, ranges)))