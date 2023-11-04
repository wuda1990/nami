import sys

while True:
    try:
        s = input()
        n = int(s)
        while n > 0:
            row = input().split()
            print(int(row[0]) + int(row[1]))
            n = n - 1
    except:
        break
