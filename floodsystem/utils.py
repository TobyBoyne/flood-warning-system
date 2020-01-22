# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def first_N_with_ties(x, N, i=None):
    """Returns first N elements of a sorted list
    If any elements after the first N have the same key value, return those elements as well
    For a list of tuples, i indexes the tuple"""

    idx = 0
    last_value = None

    while idx < len(x):
        # if N elements have been yielded, and the current element is not a tie with the previous, then stop yielding
        if idx >= N and x[i] != last_value:
            break

        yield x[i]
        idx += 1