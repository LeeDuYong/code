s = input()
ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ad = ""
res = 0
i = 0
while i < len(s):
    ad = ad + s[i]
    id = i
    for j in range(id + 1, len(s)):
        if len(ad) == 1:
            ad = ad + s[j]
            if ad == "dz":
                continue
            else:
                if ad in ca:
                    i = j
            break
        elif len(ad) == 2:
            ad = ad + s[j]
            if ad in ca:
                i = j
            break
    res = res + 1
    i = i + 1
    ad = ""
print(res)
