import fileinput
from collections import defaultdict


'''
ans = 0
S = set()
for line in fileinput.input():
    print(line)
    if len(line.strip()) == 0:
        ans += len(S)
        S = set()
    else:
        for c in line.strip(): S.add(c)
ans += len(S)
print(ans)
'''


n = 0
ans = 0
S = defaultdict(int)
for line in fileinput.input():
    if len(line.strip()) == 0:
        for k in S.keys():
            if S[k] == n: ans += 1
        S = defaultdict(int)
        n = 0
    else:
        n += 1
        for c in line.strip():
            S[c] += 1

for k in S.keys():
    if S[k] == n: ans += 1
print(ans)

