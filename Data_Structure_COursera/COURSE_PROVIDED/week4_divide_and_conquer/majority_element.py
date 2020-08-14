# Uses python3

def binary_searchr(a, x):
    l, r = 0, len(a)
    mid = ((r + l) // 2)
    mo = -1
    try:
        while x != a[mid]:
            mid = ((l + r) // 2)
            if x > a[mid]:
                l = mid
            elif x < a[mid]:
                r = mid
            if mo == mid:
                return -1
            mo = mid
    except:
        return -1
    if a[0] == x:
        return mid + binary_searchr(a[mid + 1:], x) + 1
    else:
        return mid


def binary_searchl(a, x):
    l, r = 0, len(a)
    mid = ((r + l) // 2)
    mo = -1
    try:
        while x != a[mid]:
            mid = ((l + r) // 2)
            if x > a[mid]:
                r = mid
            elif x < a[mid]:
                l = mid
            if mo == mid:
                return -1
            mo = mid
    except:
        return -1
    if a[0] == x:
        return mid + binary_searchl(a[mid + 1:], x) + 1
    else:
        return mid


def me(a, left, right):
    ri = right - 1
    le = left
    m = (ri + le) // 2
    rh = a[m:]
    lh = a[:m + 1][::-1]
    mr = binary_searchr(rh, a[m])
    ml = binary_searchl(lh, a[m])
    if (mr + ml + 1) > right / 2:
        return 1
    else:
        return 0


def na(A):
    for j in range(len(A)):
        e = A[j]
        c = 0
        for k in range(j, len(A)):
            if A[k] == e:
                c += 1
        if c > len(A) / 2:
            return 1
    return 0


# def lec(u):
#     if len(u) <=2:
#

g = int(input())
# g = 0
if g:
    A = sorted(list(map(int, input().split())))
    print(me(A, 0, len(A)))
else:
    import numpy as np
    import pandas as pd

    z = []
    for i in range(
            int(input())
    ):
        h = []
        A = sorted(list(np.random.choice(100, np.random.randint(low=1, high=100), replace=True)))
        h.append(na(A))
        h.append(me(A, 0, len(A)))
        h.append(A)
        z.append(h)
    ss = pd.DataFrame(z, columns=["r", "m", "A"])
    ss["c"] = ss["r"] == ss["m"]
    ss = ss[["r", "m", 'c', 'A']]
    ss = ss[ss["c"] == False]
    print(ss)
