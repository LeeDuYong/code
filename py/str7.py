a, b = input().split()
a = list(a)
a.reverse()
b = list(b)
b.reverse()
res = []
for i in range(len(a)):
    if int(a[i]) > int(b[i]):
        res = a
        break
    elif int(a[i]) < int(b[i]):
        res = b
        break
s = ""
for i in range(len(res)):
    s += res[i]
print(s)