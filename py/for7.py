import sys
n = int(input())
for i in range(n):
    a,b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    s = a + b
    print("Case #%d: %d" %(i + 1, s))