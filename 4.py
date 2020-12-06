ans = 0

F = ['byr', 'iyr', 'eyr', 'hgt', 'hgt', 'hcl', 'ecl', 'pid']

with open('4.in') as f:
    passports = [i for i in f.read().split('\n\n')]
    for passport in passports:
        S = {}
        print(passport)
        print(f'new pasport')
        fields = passport.split('\n')
        print(fields)

        
        for field in fields:
            li = field.split(' ')
            for f in li:
                if len(f) == 0: continue
                k, v = f.split(':')
                print(k)
                S[k] = v

        if len(S) == 8 or (len(S) == 7 and 'cid' not in S):
            ok = True
            for f in F:
                if f == 'byr':
                    ok = ok and (1920 <= int(S[f]) <= 2002)
                elif f == 'iyr':
                    ok = ok and (2010 <= int(S[f]) <= 2020)
                elif f == 'eyr':
                    ok = ok and (2020 <= int(S[f]) <= 2030)
                elif f == 'hgt':
                    if len(S[f]) <= 2:
                        ok = ok and False
                    elif S[f][len(S[f])-2:] == 'cm': ok = ok and (150 <= int(S[f][:len(S[f])-2]) <= 193)
                    else: ok = ok and (59 <= int(S[f][:len(S[f])-2]) <= 76)
                elif f == 'hcl':
                    if (len(S[f]) != 7):
                        ok = ok and False
                        continue
                    if (S[f][0] != '#'):
                        ok = ok and False
                        continue
                    ok = ok and (S[f][0] == '#')
                    ok = ok and (len([i for i in S[f][1:] if '0' <= i <= '9' or 'a' <= i <= 'f']) == 6 and len(S[f][1:]) == 6)
                elif f == 'ecl':
                    ok = ok and (S[f] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'})
                elif f == 'pid':
                    ok = ok and (len(S[f]) == 9 and len([i for i in S[f] if '0' <= i <= '9']) == 9)
            if ok: ans += 1
    print(ans)

