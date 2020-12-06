from math import prod
with open('3.in') as f:
    grid = [i.strip() for i in f.readlines()]
    H = len(grid) 
    W = len(grid[0])


    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [0 for i in range(len(slopes))]
    

    for i in range(len(slopes)):
        dx = slopes[i][0]
        dy = slopes[i][1]
        x, y = 0, 0
        ans = 0
        while True:
            x = (x + dx) % W
            y = y + dy
            if y >= H:
                trees[i] = ans
                break
            if grid[y][x] == '#': ans += 1
    print(prod(trees))
