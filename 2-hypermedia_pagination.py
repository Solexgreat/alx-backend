#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple, Dict

index_range = __import__('0-simple_helper_function').index_range


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
        """
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        pages = index_range(page, page_size)
        data = self.dataset()
        return (data[pages[0]: pages[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10)-> dict :
        """
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        [start, end] = index_range(page, page_size)
        data = self.get_page(start, end)
        next_page = None
        if page_size != 0:
            next_page = page + 1 
               
        dict_result = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': page - 1 if page > 1 else None,
            'taotal_page': total_pages
        }
        return dict_result
