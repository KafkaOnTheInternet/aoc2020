ans = 0
with open('4.in') as f:
    policies = [i.strip() for i in f.readlines()]
    for policy in policies:
        li = policy.split()
        mn, mx = [int(i) for i in li[0].split('-')]
        c = li[1][0]
        S = li[2]
        print(mn, mx, c , S)

        cnt = 0
        if S[mx-1] == c: cnt += 1
        if S[mn-1] == c: cnt += 1

        if cnt == 1: ans += 1

    print(ans)
