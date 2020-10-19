import re
cn = int(input())
for _ in range(cn):
    n, m = map(int, input().split())
    x = []
    for __ in range(n):
        x.append((input()))
    q,w = map(int, input().split())
    loc = []
    for ___ in range(q):
        loc.append((input()))
    found = False
    br = False
    i, j = 0, 0
    ino = 0
    jno = 0
    kl = -1
    mainMatrix = x[i]
    lookMatrix = loc[j]
    while not found and not br:
        pattern = lookMatrix
        fo = re.search(pattern, mainMatrix)
        print(fo)
        if kl == -1:
            foo = fo 
        if fo and fo.span() == foo.span():
            if jno < q-1:
                foo = fo
                ino += 1
                jno += 1
                mainMatrix = x[ino]
                lookMatrix = loc[jno]
                kl = 1
                continue

        elif ino != i:
            ino = i
            jno = j
            lookMatrix = loc[jno]
            kl = -1
        else:
            i += 1
            ino = i
            if ino == n:
                br = True
            else:
                mainMatrix = x[i]
        if jno == q-1:

            found = True
    if found:
        print("YES")
    else:
        print("NO")



