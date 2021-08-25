t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    res = ""
    for x in s:
        x = x * r
        res = res + x
    print(res)