s = input()
res = ""
for i in range(ord('a'), ord('z') + 1):
    res = res + str(s.find(chr(i))) + " "
print(res)