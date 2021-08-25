n = int(input())
for i in range(1, n + 1):
    e = " " * (n - i)
    s = "*" * i
    res = e + s
    print(res)