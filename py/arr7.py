c = int(input())
for i in range(c):
    li = list(map(int, input().split()))
    sum = 0
    for j in range(li[0]):
        sum = sum + li[j + 1]
    avg = sum / (li[0])
    gn = 0
    for k in range(li[0]):
        if li[k + 1] > avg:
            gn = gn + 1
    res = gn / li[0] * 100
    print("%0.3f%%" %res)