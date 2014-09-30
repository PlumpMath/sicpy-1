"""Play with Section 3.5"""

def isprime(n):
    """The method of section 1.2.6.

    Soon to be outsted by the sieve of Eratosthenes.
    """
    return n == smallest_divisor(n)

def smallest_divisor(n):
    return find_divisor(n, 2);

def find_divisor(n, test_divisor):
    if square(test_divisor) > n:
        return n
    elif divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)

def square(n):
    return n * n

def divides(a, b):
    return b % a == 0


def sum_primes_iter(a, b):
    """Sum primes in range iteratively."""
    def loop(n, accum):
        if n > b:
            return accum
        elif isprime(n):
            return loop(n + 1, accum + n)
        else:
            return loop(n + 1, accum)
    return loop(a, 0)


from functools import reduce
from operator import add
def sum_primes_seqs(a, b):
    """Sum primes using sequence transformations."""
    return reduce(add, filter(isprime, range(a, b)))


