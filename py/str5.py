s = input()
s2 = s.upper()
max = 0
res = ''
for i in range(ord('A'), ord('Z') + 1):
    n = s2.count(chr(i))
    if n > max:
        max = n
        res = chr(i)
    elif n == max:
        res = '?'
print(res)
"""
li = []
for i in range(26):
    li.append(0)
for i in s:
    li[ord(i) - ord('A')] = li[ord(i) - ord('A')] + 1

max = 0
maxID = 0
for i in li:
    if li[i] > max:
        max = li[i]
        maxID = i
print(str(i + ord('A')))
"""