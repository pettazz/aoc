jolts = 0

with open('input.txt') as f:
  banks = [list(map(int, line.strip())) for line in f]

  for bank in banks:
    # find the largest number (excluding last, must have 2 digits)
    largest = None
    for idx, j in enumerate(bank[:-1]):
      if largest is None or j > largest[1]:
        largest = (idx, j)

    # find the largest number to its right in the list
    j2 = max(bank[largest[0]+1:])
    jolts += int(str(largest[1]) + str(j2))

print(jolts)