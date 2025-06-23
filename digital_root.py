def digital_root(n):
    s = 0
    p = n
    a = True

    while p != 0:
        t = p % 10
        s += t
        p //= 10

        if s >= 10:
            a = False

    if not a:
        return digital_root(s)
    else:
        return s