def find_next_largest(bank, iter = 12):
  if iter == 0:
    return ""

  largest = None
  for idx, j in enumerate((bank[:-(iter-1)] if iter > 1 else bank)):
    if largest is None or j > largest[1]:
      largest = (idx, j)
  return str(largest[1]) + find_next_largest(bank[largest[0]+1:], iter - 1)

with open('input.txt') as f:
  banks = [list(map(int, line.strip())) for line in f]
  print(sum([int(find_next_largest(bank)) for bank in banks]))
