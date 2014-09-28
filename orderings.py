"""Inspired by the beginning of Section 3.4.2."""

def orderings(p1, p2):
    """All interleavings of two sequences.

    >>> orderings(['a'], ['x'])
    [['a', 'x'], ['x', 'a']]
    >>> orderings(['a'], ['x','y'])
    [['a', 'x', 'y'], ['x', 'a', 'y'], ['x', 'y', 'a']]
    >>> len(orderings(['a','b','c'], ['x','y','z']))
    20
    """
    assert len(p1) > 0 and len(p2) > 0, "Sequences must have elements."
    if len(p1) == 1:
        result = []
        for i in range(len(p2)+1):
            cpy = p2[:]
            cpy.insert(i, p1[0])
            result.append(cpy)
        return result
    else:
        partials = orderings(p1[1:], p2)
        result = []
        # For each partial ordering, find all complete orderings -- that is,
        # orderings that include p1[0] and that place p1[0] before p1[1].
        for partial in partials:
            # You can always put p1[0] at the front.
            cpy = partial[:]
            cpy.insert(0, p1[0])
            result.append(cpy)
            i = 1
            while partial[i-1] != p1[1]:
                cpy = partial[:]
                cpy.insert(i, p1[0])
                result.append(cpy)
                i += 1
        return result
