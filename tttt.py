s, x = list(map(int, input().split()))
c = 1

while s // x != 0:
    s = s // x
    c += 1

print(c)
