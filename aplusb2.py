import sys

while True:
    try:
        s = input('please input the the number:')
        n = int(s)
        while n > 0:
            row = input("please input a and b:").split()
            print(int(row[0]) + int(row[1]))
            n = n - 1
    except:
        break
