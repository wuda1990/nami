import sys

for line in sys.stdin:
    l = list(map(int, line.split()))
    if l[0] == 0:
        break
    res = 0
    for x in l[1:l[0] + 1]:
        res += x
    print(res)
