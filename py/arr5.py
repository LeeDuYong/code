n = int(input())
li = list(map(int, input().split()))
max = 0
nSum = 0
for x in li:
    if x > max:
        max = x
adj = 100 / max
for i in range(len(li)):
    nSum = nSum + li[i] * adj
res = nSum / len(li)
print(res)