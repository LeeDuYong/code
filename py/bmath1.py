a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if b >= c:
    print(-1)
else:
    res = 0
    ch = False
    si = c - b
    res = a // si + 1
    print(res)