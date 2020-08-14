def getPattern(x):
    p = [x[0]]
    h = True
    i = 1
    while h:
        c = len(p)
        ff = x[c:c + c]
        if len(ff) < c:
            p += ff
            h = False
        elif ff == p:
            h = False
        else:
            p.append(x[c])
            i = 1
        i += 1
    return p


def calc_fib(n):
    if n == 0:
        return 0
    p = 0
    c = 1
    for i in range(1, n):
        p, c = c, (c + p)
    return c



n = int(input())
d = []
for i in range(120):
    d.append(calc_fib(i) % 10)
p = getPattern(d)
print(p[n % len(p)])




