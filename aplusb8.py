while 1:
    try:
        n = int(input())
        if n == 0:
            break
        row = list(map(int, input().split()))
        average = sum(row[0:]) // n
        result = 0
        for element in row:
            if element > average:
                result = result + element - average
        print(result)
        print()
    except Exception as e:
        # print("repr(e):\t", repr(e))
        break
