import fileinput
ans = -1 
ids = set()
ids_last = set()
for line in fileinput.input():
    row, col = 0, 0
    lo, hi, mid = 0, 127, -1
    for c in line[:7]:
        if c == 'F':
            mid = (hi + lo) // 2
            hi = mid
        else:
            mid = (hi + lo) // 2
            lo = mid + 1
    row = lo 
    lo, hi, mid = 0, 7, -1
    for c in line[7:]:
        if c == 'R':
            mid = (hi + lo) // 2
            lo = mid + 1
        else:
            mid = (hi + lo) // 2
            hi = mid
    col = lo
    ans = max(ans, row*8 + col)
    if row == 0 or row == 127:
        ids_last.add(row*8 + col)
    else:
        ids.add(row*8 + col)
print(ans)
mn, mx = min(ids), max(ids)
for i in range(mn+1, mx):
    if i not in ids_last and i not in ids:
        print(i)
        break




