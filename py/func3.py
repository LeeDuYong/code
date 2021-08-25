def HanNum(n):
    if n < 100:
        return n
    elif n <= 110:
        return 99
    res = 99
    for x in range(100, n + 1):
        pf = x % 10 
        ps = (x // 10) % 10
        pt = x // 100
        if (pt - ps) == (ps - pf):
            res = res + 1
    return res

n = int(input())
ret = HanNum(n)
print(ret)