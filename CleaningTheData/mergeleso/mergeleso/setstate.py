"""Script to merge LESO data files."""
import pandas as pd
import re
import sys, traceback

# DEFAULTS & EXPECTED

state_dict = {0:'No values found in file.',
              100:'No expected or unique values.',
              110:'No expected values, but all are unique.',
              120:'No expected values, but some are unique.',
              101:'All expected values, but none are unique.',
              111:'All expected values, and all are unique.',
              121:'All expected values, and some are unique.',
              102:'Some missing values, and none are unique.',
              112:'Some missing values, and all are unique.',
              122:'Some missing values, and some are unique.',
              103:'Some missing & unexpected values, and none are unique.',
              113:'Some missing & unexpected values, and all are unique.',
              123:'Some missing & unexpected values, and some are unique.',
              104:'Some unexpected values, and none are unique.',
              114:'Some unexpected values, and all are unique.',
              124:'Some unexpected values, and some are unique.',
              -999:'Missing expected values.'}



# FUNCTIONS
def is_nonempty(a_list: list) -> int:
    """ Returns 1 if a set is empty.
    >>> is_nonempty([])
    0
    >>> is_nonempty([1])
    1
    """
    return 1 if a_list else 0


def is_disjoint(a_set: set, b_set: set) -> int:
    """ Returns 1 if two non-empty sets are disjoint.
    >>> is_disjoint({1},{1})
    0
    >>> is_disjoint({1},{2})
    1
    >>> is_disjoint({1,2},{1})
    0
    >>> is_disjoint({1},{1,2})
    0
    >>> is_disjoint({1,2},{2,3})
    0
    """
    return 1 if (a_set.isdisjoint(b_set)) else 0


def is_superset(a_set: set, b_set: set) -> int:
    """ Returns 1 if non-empty set a is a proper superset of non-empty set b.
    >>> is_superset({1},{1})
    0
    >>> is_superset({1},{2})
    0
    >>> is_superset({1,2},{1})
    1
    >>> is_superset({1},{1,2})
    0
    >>> is_superset({1,2},{2,3})
    0
    """
    return 1 if (a_set) > (b_set) else 0


def is_subset(a_set: set, b_set: set) -> int:
    """ Returns 1 if non-empty set a is a proper subset of non-empty set b.
    >>> is_subset({1},{1})
    0
    >>> is_subset({1},{2})
    0
    >>> is_subset({1,2},{1})
    0
    >>> is_subset({1},{1,2})
    1
    >>> is_subset({1,2},{2,3})
    0
    """
    return 1 if (a_set) < (b_set) else 0


def is_equal(a_set: set, b_set: set) -> int:
    """ Returns 1 if two non-empty sets are equal.
    >>> is_equal({1},{1})
    1
    >>> is_equal({1},{2})
    0
    >>> is_equal({1,2},{1})
    0
    >>> is_equal({1},{1,2})
    0
    >>> is_equal({1,2},{2,3})
    0
    """
    return 1 if (a_set) == (b_set) else 0
        

def split_uniqueness(a_list: list):
    """ Splits a non-empty list into three sets:\
        {unique elements}, {non-duplicate elements}, {duplicate elements}.
    NOTE: this could be done with pandas Series  a_series[a_series.duplicated()]
    >>> split_uniqueness([1])
    ({1}, {1}, set())
    >>> split_uniqueness([1,1])
    ({1}, set(), {1})
    >>> split_uniqueness([1,1,2])
    ({1, 2}, {2}, {1})
    """
    set_alist = set(a_list)
    track_duplicates = a_list.copy()
    for val in set_alist:
        track_duplicates.remove(val)
    set_duplicates = set(track_duplicates)
    set_noduplicates = set_alist.difference(set_duplicates)
    return set_alist, set_noduplicates, set_duplicates


def state_unique(noduplicates: set, duplicates: set) -> int:
    """ Returns 0 if all are duplicates, 1 if no duplicates, 2 if some duplicates.
    >>> state_unique({1},{2})
    2
    >>> state_unique({1},{})
    1
    >>> state_unique({},{1})
    0
    """
    if (is_nonempty(noduplicates) == 1):
        state = (is_nonempty(duplicates) + 1)
    else:
        state = 0
    return state


def state_expected(actual: set,expected: set) -> int:
    """ Returns int representating the relationship between two non-empty sets.
    >>> state_expected({2},{1})
    0
    >>> state_expected({1},{1})
    1
    >>> state_expected({1},{1,2})
    2
    >>> state_expected({2,3},{1,2})
    3
    >>> state_expected({1,2},{1})
    4
    """
    if (is_equal(actual,expected) == 1):
        state = 1
    elif (is_subset(actual,expected) == 1):
        state = 1 + 1
    elif (is_disjoint(actual,expected) == 0):
        state = (is_subset(expected,actual) + 3)
    else:
        state = 1 - 1
    return state


def state_of_list(actual_list: list,expected_set: set) -> int:
    """ Returns integer representation of the relationship between a list and a non-empty set.
    >>> state_of_list([],{})
    -999
    >>> state_of_list([1],{})
    -999
    >>> state_of_list([],{1})
    0
    >>> state_of_list([1],{1})
    111
    >>> state_of_list([2],{1})
    110
    >>> state_of_list([1,1],{1})
    101
    >>> state_of_list([1,1],{1,2})
    102
    """
    if not expected_set:
        return -999
    unique, noduplicates, duplicates = set(),set(),set()
    # Q1 is list non-empty? yes continue, no fall out
    cumulative_state = is_nonempty(actual_list) * 100
    if cumulative_state > 0:
        unique, noduplicates, duplicates = split_uniqueness(actual_list)
        # Q2 are the sheet names unique?
        cumulative_state = cumulative_state + (state_unique(noduplicates, duplicates) * 10)
        # Q3 ignoring duplicates, are there any unexpected sheets/state names?
        cumulative_state = cumulative_state + (state_expected(unique,expected_set) * 1)
    return cumulative_state        



#TEST actual_list = [[],[1],[2],[1,2],[2,3],[1,1],[1,1,2],[1,2,2],[2,2,3],[2,3,3]]
#TEST expected_list = [set([1]),set([1,2])]

if __name__ == '__main__':
    import doctest      #for inline testing
    doctest.testmod()   #for inline testing
