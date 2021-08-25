t = int(input())
res = 0
for i in range(t):
    w = input()
    li = []
    ch = True
    temp = '@'
    for k in w:
        if k not in li:
            li.append(k)
        elif k != temp:
            ch = False
            break
        temp = k
    if ch == True:
        res = res + 1
print(res)