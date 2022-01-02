call = input()
time = 0
for i in range(len(call)):
  if call[i] in ['A', 'B', 'C']:
    time += 3
  elif call[i] in ['D', 'E', 'F']:
    time += 4
  elif call[i] in ['G', 'H', 'I']:
    time += 5
  elif call[i] in ['J', 'K', 'L']:
    time += 6
  elif call[i] in ['M', 'N', 'O']:
    time += 7
  elif call[i] in ['P', 'Q', 'R', 'S']:
    time += 8
  elif call[i] in ['T', 'U', 'V']:
    time += 9
  else:
    time += 10

print(time)