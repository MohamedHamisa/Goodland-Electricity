def pylons(k, arr):
    prev, curr = -2*k, -k
    out = 0
    for i, el in enumerate(arr):
        if i - curr >= 2*k:
            return -1
        if el:
            if i - prev >= 2*k:
                prev = curr
                out += 1
            curr = i
    return out

