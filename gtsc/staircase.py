# a staircase has n steps, you may walk 1 or 2 steps, how many ways can you get to the top?


"""
              _
            _|
          _|
        _|

let's first do some example,
n =1
only 1

n = 2
1, 1
2

n=3
1, 1, 1,
1, 2,
2, 1

Question is how do you generalize your method to solve an arbitrary height staircase?

pause a couple of minutes for students to think

1) you could start from take all one-step, then gradually change last step from 1 to 2, until
all your steps becomes 2. like this
1 1 1 1 1
1 1 1 2 
1 1 2 1
1 2 1 1
1 2 2
2 1 2
2 2 1

the method seems natural, but ...

we want to ensure
a) we exhaust all possibilities
b) no duplicates

it's tricky to ensure the two...
when it's tricky, often the implementation is error-prone.

2) let's take a step back, think about alternative ways...

let f(n) represent the total steps need to reach the top of n-level staircase.

can we divide the problem?

to get to level n, you either get to n-1 or n-2 since 1 or 2 steps are allowed.

a) when you reach level n-1, you don't have any choice but walk the last step.

b) when you reach level n-2, you could go two 1-step, or go one 2-step.

but if you take 1 step from n-2 to reach n-1, your solution becomes a duplicate to a).

so to remove duplicates, when you reach n-2, you take a 2-level step.

therefore, we conclude

f(n) = f(n-1) + f(n-2)

if n = 3, we can get

f(3) = f(2) + f(1)

f(1) = 1, f(2) = 2, therefore f(3) = 3

"""


level = 0
def trace(f):
    def g(*args):
        global level
        # pretty print indicating the level
        prefix = "|  " * level + "|--"
        strargs = ", ".join(repr(a) for a in args)
        print("{} {}({})".format(prefix, f.__name__, strargs))
        # increment the level before calling the function
        # and decrement it after the call
        level += 1
        result = f(*args)
        level -= 1
        return result
    return g


@trace
def f(n):
    if n > 2:
        return f(n-1) + f(n-2)

    else:
        return n


def f2(n):
    """
    a bottom up approach
    can we figure out 1, 2, ... n?
    1 2 3 5 ...
    """
    if n < 3:
        return n

    a, b = 1, 2

    for _ in range(2, n):
        a, b = b, a+b

    return b


print(f(4))

# concepts: recursive, iterative, divide and conquer, top down, bottom up
# key: divide the problem, find the relationship between original problem and new problem
# note the time complexity of the two solution

