def collaz(n, a=0):
    if n == 1:
        print(a)
        return 1
    elif n % 2 == 0:
        return collaz(n // 2, a + 1)
    else:
        return collaz(3 * n + 1, a + 1)

collaz(5)

