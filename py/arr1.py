max = -1000000
min = 1000000
n = int(input())
a = input().split()
for i in a:
    ni = int(i)
    if ni > max:
        max = ni
    if ni < min:
        min = ni
print(min, max)