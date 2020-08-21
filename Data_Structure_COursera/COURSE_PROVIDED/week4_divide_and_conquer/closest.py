# Uses python3

def srtx(x, y):
    a = x[0]
    b = y[0]
    z = x[1]
    w = y[1]
    m = len(a)
    n = 0
    f = True
    for i in range(len(b)):
        while n < len(a):
            if b[i] <= a[n]:
                a.insert(n, b[i])
                z.insert(n, w[i])
                f = False
                n += 1
                d = i
                break
            n += 1
        if n == len(a) and f:
            a = a + b
            z = z + w
            d = -1
            break
    if len(a) != m + len(b):
        a = a + (b[d + 1:])
        z = z + (w[d + 1:])
    return a, z


def srty(x, y):
    a = x[0]
    b = y[0]
    z = x[2]
    w = y[2]
    m = len(a)
    n = 0
    f = True
    for i in range(len(b)):
        while n < len(a):
            if b[i] <= a[n]:
                a.insert(n, b[i])
                z.insert(n, w[i])
                f = False
                n += 1
                d = i
                break
            n += 1
        if n == len(a) and f:
            a = a + b
            z = z + w
            d = -1
            break
    if len(a) != m + len(b):
        a = a + (b[d + 1:])
        z = z + (w[d + 1:])
    return a, x[1] + y[1], z


def quick_sortx(a, b):
    if len(a) == 1:
        return a, b
    return srtx(quick_sortx(a[len(a) // 2:], b[len(b) // 2:]), quick_sortx(a[:len(a) // 2], b[:len(b) // 2]))


def quick_sorty(a, b, index):
    if len(a) == 1:
        return a, b, index
    return srty(quick_sorty(a[len(a) // 2:], b[len(b) // 2:], index[len(a) // 2:]),
                quick_sorty(a[:len(a) // 2], b[:len(b) // 2], index[:len(a) // 2]))


def minimum_distance(x, y, k, d=2828427125):
    if len(x) == 3:
        f1 = (((x[0] - x[2]) ** 2) + ((y[0] - y[2]) ** 2)) ** 0.5
        f2 = (((x[1] - x[2]) ** 2) + ((y[2] - y[2]) ** 2)) ** 0.5
        f3 = (((x[0] - x[1]) ** 2) + ((y[0] - y[1]) ** 2)) ** 0.5
        return x, y, k, min(f1, f2, f3, d)
    elif len(x) == 2:
        f = (((x[0] - x[1]) ** 2) + ((y[0] - y[1]) ** 2)) ** 0.5
        return x, y, k, min(f, d)
    elif len(x) == 1:
        return x, y, k, d
    else:
        ss = quick_sortx(x, y)
        # k = [j for j in range(len(x))]
        x1 = (ss[0][len(ss[0]) // 2:], ss[1][len(ss[0]) // 2:], k[len(ss[0]) // 2:])
        x2 = (ss[0][:len(ss[0]) // 2], ss[1][:len(ss[0]) // 2], k[:len(ss[0]) // 2])
        # print(x1,x2)
        x1s = quick_sorty(x1[1], x1[0], x1[2])
        x2s = quick_sorty(x2[1], x2[0], x2[2])
        import matplotlib.pyplot as plt
        h1 = ([ss[0][i] for i in x1s[2][len(x1s[0]) // 2:]], x1s[0][len(x1s[0]) // 2:], x1s[2][len(x1s[0]) // 2:])
        h2 = ([ss[0][i] for i in x1s[2][:len(x1s[0]) // 2]], x1s[0][:len(x1s[0]) // 2], x1s[2][:len(x1s[0]) // 2])
        h3 = ([ss[0][i] for i in x2s[2][len(x2s[0]) // 2:]], x2s[0][len(x2s[0]) // 2:], x2s[2][len(x2s[0]) // 2:])
        h4 = ([ss[0][i] for i in x2s[2][:len(x2s[0]) // 2]], x2s[0][:len(x2s[0]) // 2], x2s[2][:len(x2s[0]) // 2])
        plt.figure()
        plt.scatter(x1[0],x1[1],s=300)
        plt.scatter(h1[0], h1[1])
        plt.scatter(h4[0], h4[1])
        plt.scatter(h2[0], h2[1])
        plt.scatter(h3[0], h3[1])
        plt.legend(["x1","h1",'h4','h2','h3'],loc=0)
        plt.show()
        # print([hj for hj in [h1,h2,h3,h4]])
        f2 = (((h1[0][0] - h3[0][-1]) ** 2) + ((h1[1][0] - h3[1][-1]) ** 2)) ** 0.5
        f4 = (((h4[0][-1] - h2[0][0]) ** 2) + ((h4[1][-1] - h2[1][0]) ** 2)) ** 0.5
        f3 = (((h4[0][-1] - h3[0][0]) ** 2) + ((h4[1][-1] - h3[1][0]) ** 2)) ** 0.5
        f1 = (((h1[0][-1] - h2[0][-1]) ** 2) + ((h1[1][-1] - h2[1][-1]) ** 2)) ** 0.5
        fx = (((x2[0][-1] - x1[0][0]) ** 2) + ((x2[1][-1] - x1[1][0]) ** 2)) ** 0.5
        g = min(f1, f2, f3, f4, fx)
        z = minimum_distance(h1[0], h1[1], [j for j in range(len(h1[0]))], g)
        w = minimum_distance(h2[0], h2[1], [j for j in range(len(h2[0]))], g)
        u = minimum_distance(h3[0], h3[1], [j for j in range(len(h3[0]))], g)
        t = minimum_distance(h4[0], h4[1], [j for j in range(len(h4[0]))], g)
        # if z[3]<=w[3]:
        return z, w, u, t


x = []
y = []
n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    x.append(data[0])
    y.append(data[1])
k = [i for i in range(len(x))]
# print("{0:.9f}".format(minimum_distance(x, y)))
bm = (minimum_distance(x, y, k))
print(bm)
s = 2828427125
for i in bm:
    if i[3] < s:
        s = i[3]
print(s)
