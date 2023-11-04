while True:
    try:
        n = int(input())
        for i in range(n):
            row = list(map(int, input().split()))
            m = row[0]
            print(sum(row[-m:]))
            if i < n - 1:
                print()
    except Exception as e:
        print("repr(e):\t", repr(e))
        break
