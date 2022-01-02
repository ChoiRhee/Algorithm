string = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'nj', 'lj', 's=', 'z=']
cnt = 0

for c in cro:
  if c in string:
    string = string.replace(c, '!')

print(len(string))