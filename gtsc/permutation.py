def permute(a):
    if len(a)<2:
        yield a
    else:
        x = a[-1:] # x is the last element
        for p in permute(a[:-1]):
            for i in range(len(a)):
                yield p[:i] + x + p[i:]


print(list(permute("abc")))