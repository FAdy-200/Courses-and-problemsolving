# Uses python3
# TODO UNDERSTAND THIS MORE
def g(x, y):
    return int(str(x) + str(y)) >= int(str(y) + str(x))


def largest_number(a):
    an = []
    while len(a) != 0:
        ma = ""
        for i in a:
            if g(i, ma):
                ma = i
        an.append(str(ma))
        a.remove(ma)
    return "".join(an)


n = int(input())
x = list(map(int, input().split()))
print(largest_number(x))
