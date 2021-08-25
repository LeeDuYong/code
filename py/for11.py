n, x = input().split()
n = int(n)
x = int(x)
li = input().split()
res = ""
for i in li:
    ni = int(i)
    if ni < x:
        res = res + i + " "
print(res)