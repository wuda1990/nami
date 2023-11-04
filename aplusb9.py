while 1:
    try:
        n = int(input())
        result = 0
        while n:
            value = n % 10
            result += value if value % 2 == 0 else 0
            n = n // 10
        print(result)
        print()
    except Exception as e:
        # print("repr(e):\t", repr(e))
        break
