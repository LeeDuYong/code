li = []
max = 0
maxIdx = 0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        maxIdx = i + 1
    li.append(a)
print(max)
print(maxIdx)