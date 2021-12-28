from string import ascii_lowercase
 
alpha = list(ascii_lowercase)
strs = input()

out = []
for a in alpha:
  if a in strs:
    out.append(str(strs.index(a)))
  else:
    out.append('-1')

print(' '.join(out))