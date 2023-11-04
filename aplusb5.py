import sys

# for line in sys.stdin:
#     l = list(map(int, line.split()))
#     print(l[0]+l[1])
#     print()

while True:
    try:
        l = list(map(int, input().split()))
        print(l[0] + l[1])
        print()
    except:
        break
