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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns a dictionary containing the following key-value pairs """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        total_rows = len(self.__dataset)
        total_pages = math.ceil(total_rows / page_size)

        if page + 1 > total_pages:
            next_page = None
        else:
            next_page = page + 1

        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1

        data = self.get_page(page, page_size)

        result_dict = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return result_dict
