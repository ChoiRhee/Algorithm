from collections import Counter
string = input().lower()
cnt = Counter(string).most_common(2)

if len(cnt) == 1:
    print(string.upper())
elif cnt[0][1] == cnt[1][1]:
    print('?')
else:
    print(cnt[0][0].upper())