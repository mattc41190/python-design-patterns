import functools

def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    
    return memoizer

# naive function we can decorate with memoize

@memoize
def fibonacci(n):
    '''finds the nth number in the fibonacci sequence'''
    assert(n >= 0), 'n must be greater than or equal to 0'
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)

@memoize
def nsum(n):
    '''find the sum of all number up to n'''
    assert(n >= 0), 'n must be greater than or equal to 0'
    return 0 if n == 0 else n + nsum(n-1)


# regularly memoized functions
# known_sum = {0:0}
# def nsum(n):
#     assert(n >= 0), 'n must be >= 0'
#     if n in known_sum:
#         return known_sum[n]
#     res = n + nsum(n-1)
#     known_sum[n] = res
#     return res

# known_fib = {0:0, 1:1}
# def fibonacci(n):
#     '''finds the nth number in the fibonacci sequence'''
#     assert(n >= 0), 'n must be greater than or equal to 0'
#     if n in known_fib:
#         return known_fib[n]
#     res = fibonacci(n-1) + fibonacci(n-2)
#     known_fib[n] = res
#     return res