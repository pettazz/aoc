zeros = 0
pointer = 50

with open('input.txt') as f:
  for line in f:
    wraps = divmod(int(line[1:]), 100)
    zeros += wraps[0]
    clicks = wraps[1]

    startpoint = pointer
    if line[0] == 'L':
      clicks = 0 - clicks
    pointer = pointer + clicks

    if pointer < 0:
      pointer = 100 + pointer
      # dont count it as "passing" 0 again if we started there
      if startpoint != 0:
        zeros += 1
    elif pointer > 99:
      pointer = pointer - 100
      zeros += 1
    elif pointer == 0:
      zeros += 1

print(zeros)
