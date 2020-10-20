import re
cn = int(input())
for _ in range(cn):
    n, m = map(int, input().split())
    x = ""
    for __ in range(n):
        x = x+"."+input()
    q, w = map(int, input().split())
    loc = "("+input()+")"
    for ___ in range(q-1):
        loc = loc+".{"+format(m-w+1)+"}"+"("+input()+")"
    # print(loc)
    # print(x)
    se = re.search(loc, x)
    if se:
        print("YES")
    else:
        print("NO")



