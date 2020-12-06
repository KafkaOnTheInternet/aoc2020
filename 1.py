with open('3.in') as f:
    nums = [int(i.strip()) for i in f.readlines()]
    for i in nums:
        n = 2020-i
        dp = set()
        for j in nums:
            if j == i: continue
            dp.add(j)
        for j in nums:
            if (n-j) in dp:
                print((n-j)*j*(i))
                exit()
