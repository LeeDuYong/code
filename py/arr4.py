li = []
cnt = 0
for i in range(10):
    a = int(input())
    rm = a % 42
    if rm not in li:
        li.append(rm)
        cnt = cnt + 1
print(cnt)