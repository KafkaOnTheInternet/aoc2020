import fileinput
mx, mn = -1, 10e5
sub = {'B':'1', 'F':'0', 'R':'1', 'L':'0'}
ids = set()
for line in fileinput.input():
    val = int(''.join([sub[i] for i in line.strip()]), 2)
    mx = max(mx, val)
    mn = min(mn, val)
    ids.add(val)
print(f'P1: {mx}')
ans = set(list(range(mn, mx+1))) - ids
print(f'P2: {ans}')


