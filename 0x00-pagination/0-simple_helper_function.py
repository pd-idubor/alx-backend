#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Return tuple containing a start index and an end
    index corresponding to the range of indexes to return in
    a list for those particular pagination parameters"""
    end: int = page * page_size
    st: int = end - page_size
    return (st, end)
