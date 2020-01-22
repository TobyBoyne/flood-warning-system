"""Unit test for the utils module"""

import floodsystem.utils


def test_sort():
    """Test sort container by specific index"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2)
    assert list1[0] == b
    assert list1[1] == a
    assert list1[2] == c


def test_reverse_sort():
    """Test sort container by specific index (reverse)"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2, reverse=True)
    assert list1[0] == c
    assert list1[1] == a
    assert list1[2] == b


def test_first_N_with_ties():
    """Test the function first_N_with_ties()
    Input must be a sorted list of tuples
    The output should have length 3 (due to tie of b and c)"""

    my_list = [
        ('a', 9),
        ('b', 7),
        ('c', 7),
        ('d', 5)
    ]

    first_N = floodsystem.utils.first_N_with_ties(my_list, 2, 1)

    assert list(first_N) == [('a', 9), ('b', 7), ('c', 7)]