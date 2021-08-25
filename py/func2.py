def self_num(n):
    li = list(range(1, n + 1))
    cnum = 0
    cons = 1
    while cons < n:
        cnum = cons
        rm = cons
        while rm > 0:
            cnum = cnum + rm % 10
            rm = rm // 10
        cons = cons + 1
        if cnum in li:
            li.remove(cnum)
    return li
    
res = self_num(10000)
for i in range(len(res)):
    print(res[i])