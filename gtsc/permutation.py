def permute(a):
    if len(a)<2:
        yield a
    else:
        x = a[-1:] # x is the last element
        for p in permute(a[:-1]):
            for i in range(len(a)):
                yield p[:i] + x + p[i:]


print(list(permute("abc")))

#
# take list a, generate permutations
# algorithm: for example, to generate permutation [1 2 3]
# say we already know how to permutation [1 2], which is
# 1 2
# 2 1
# for each permutation, add 3 in this way:
# now walk 3 from position last to first
# 1 2 3
# 1 3 2
# 3 1 2
#
# if n is 1, print it and return

def permute2(a):
    result = []
    if len(a)<2:
        return a
    else:
        x = a[-1:] # x is the last element
        for p in permute(a[:-1]):
            for i in range(len(a)):
                result.append(p[:i] + x + p[i:])
    return result