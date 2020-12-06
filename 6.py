import fileinput
from collections import defaultdict

uni = set()
intr = set()

ans1 = 0
ans2 = 0

for line in fileinput.input():
    if len(line.strip()) == 0:
        ans1 += len(uni)
        ans2 += len(intr)
        uni = set()
        intr = set()
    elif len(uni) == 0:
        uni = set(line.strip())
        intr = set(line.strip())
    else:
        uni = uni | set(line.strip())
        intr = intr & set(line.strip())
ans1 += len(uni)
ans2 += len(intr)

print(f'p1: {ans1}')
print(f'p2: {ans2}')

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
'''
