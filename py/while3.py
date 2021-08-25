a = int(input())
b = a
cnt = 0
while True:
    f = (b % 10) * 10
    s = (b // 10 + b % 10) % 10
    b = f + s
    cnt = cnt + 1
    if b is a:
        break
print(cnt)