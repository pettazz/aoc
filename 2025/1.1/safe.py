zeros = 0
pointer = 50

with open('input.txt') as f:
  for line in f:
    clicks = int(line[1:]) % 100
    if line[0] == 'L':
      clicks = 0 - clicks
    pointer = pointer + clicks
    if pointer < 0:
      pointer = 100 + pointer
    elif pointer > 99:
      pointer = pointer - 100

    if pointer == 0:
      zeros += 1

print(zeros)
