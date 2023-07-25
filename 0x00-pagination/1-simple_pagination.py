#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return tuple containing a start index and an end
    index corresponding to the range of indexes to return in
    a list for those particular pagination parameters"""
    end: int = page * page_size
    st: int = end - page_size
    return (st, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """Return index range of indexes to return in a list
        for given pagination parameters"""
        end: int = page * page_size
        st: int = end - page_size
        return (st, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Use index_range to find the correct indexes to
        paginate the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert (page > 0 and page_size > 0)
        st, end = Server.index_range(page, page_size)
        return self.dataset()[st:end]
