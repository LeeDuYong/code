a, b = input().split()
mt = 24*60
h = int(a)
m = int(b)
t = h*60 + m
nt = t - 45
if nt < 0:
    nt = mt + nt
nh = nt//60
nm = nt%60
print(nh, nm)