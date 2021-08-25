s = input()
res = 0
for i in s:
    n = ord(i) - ord('A')
    t = 2
    if n < 15:
        t = t + n // 3 + 1
    elif n < 19:
        t = t + 6
    elif n < 22:
        t = t + 7
    elif n < 26:
        t = t + 8
    res = res + t
print(res)