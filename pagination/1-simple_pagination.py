#!/usr/bin/env python3
""" Function that returns a tuple containing
the start index and the end index """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ Calculates start rate and end rate """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        if self.__dataset is None:
            self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(self.__dataset):
            return []

        page_data = self.__dataset[start_index:end_index]
        return page_data
