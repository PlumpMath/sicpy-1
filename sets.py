"""Mostly lifted from http://composingprograms.com/pages/29-recursive-objects.html."""

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({0}{1})'.format(self.first, rest)

class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.entry, self.branches)
        else:
            return 'Tree({0})'.format(repr(self.entry))


# Sets as unordered sequences.

def empty(s):
    return s is Link.empty

def set_contains(s, v):
    """Return True iff set s contains v.

    O(n) time.

    >>> s = Link(3, Link(4, Link(5)))
    >>> set_contains(s, 2)
    False
    >>> set_contains(s, 5)
    True
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def adjoin_set(s, v):
    """Return a set containing all elements of s and element v.

    O(n) time.

    >>> s = Link(3, Link(4, Link(5)))
    >>> adjoin_set(s, 2)
    Link(2, Link(3, Link(4, Link(5))))
    """
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)

def keep_if_link(pred, s):
    """Filter set s using predicate pred."""
    if empty(s):
        return s
    elif pred(s.first):
        return Link(s.first, keep_if_link(pred, s.rest))
    else:
        return keep_if_link(pred, s.rest)

def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    if empty(s):
        return s
    else:
        return Link(f(s.first), apply_to_all_link(f, s.rest))

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    if empty(s):
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    O(n**2) time.

    >>> s = Link(3, Link(4, Link(5)))
    >>> t = Link(2, Link(3, Link(4, Link(5))))
    >>> intersect_set(s, apply_to_all_link(lambda x: x * x, t))
    Link(4)
    """
    return keep_if_link(lambda v: set_contains(set2, v), set1)

def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    O(n**2) time.

    >>> s = Link(3, Link(4, Link(5)))
    >>> t = Link(2, Link(3, Link(4, Link(5))))
    >>> union_set(s, t)
    Link(2, Link(3, Link(4, Link(5))))
    """
    set1_not_set2 = keep_if_link(lambda v: not set_contains(set2, v), set1)
    return extend_link(set1_not_set2, set2)
