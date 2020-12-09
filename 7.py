import fileinput
from collections import defaultdict

G = defaultdict(list)
RG = defaultdict(list)
C = set()



p1 = 0
p2 = 0

def dfs1(i):
    global G
    global C
    C.add(i)
    for j in G[i]:
        if j not in C:
            dfs1(j)


def dfs2(i):
    global RG
    global C
    num_bags = 0
    C.add(i)
    for j, w in RG[i]:
        num_bags += w + w*dfs2(j) 
    return num_bags


src = 'shiny gold'

for line in fileinput.input():
    words = [i for i in line.strip().split(' ')]
    if words[-3] == 'no':
        continue
    for i in range(2, len(words)):
        u = words[0] + ' ' + words[1]
        if words[i].isdigit():
            v = words[i+1] + ' ' + words[i+2]
            G[v].append(u)
            RG[u].append([v, int(words[i])])

dfs1(src)

p1 = len(C) - 1

C = set()

p2 = dfs2(src)
print(p1, p2)



