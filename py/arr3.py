li = [0,0,0,0,0,0,0,0,0,0]
a = int(input())
b = int(input())
c = int(input())
mul = a * b * c
while mul > 0:
    k = mul % 10
    li[k] = li[k] + 1
    mul = mul // 10
for i in li:
    print(i)