"""Count ways to make change for cent amounts using sets of coins.

Inspired by the 'Counting change' example in Section 1.2.2.
"""

def memoize(f):
    """Memoize a function of positional arguments."""
    cache = {}
    def helper(*args):
        if tuple(args) not in cache:
            cache[tuple(args)] = f(*args)
        return cache[tuple(args)]
    return helper

COMMON_COINS = frozenset([1,5,10,25,100])
ONE_DOLLAR = 100

@memoize
def count_ways(cents, coins):
    """Count ways to make change for cent amounts using sets of coins.

    >>> count_ways(ONE_DOLLAR, COMMON_COINS)
    243
    >>> ([count_ways(n * ONE_DOLLAR, COMMON_COINS) for n in range(1,101)])[99]
    3430874151
    """
    assert type(cents) == int, 'Give cents as an integer'
    assert type(coins) == frozenset, 'Coins must be a (immutable) frozenset'
    coins = set(coins)
    if cents == 0:
        return 1
    elif cents < 0:
        return 0
    elif len(coins) == 0:
        return 0
    else:
        coin = coins.pop()
        fewer_coins = frozenset(coins)
        coins.add(coin)
        all_coins = frozenset(coins)
        return (count_ways(cents - coin, all_coins) +
                count_ways(cents, fewer_coins))
