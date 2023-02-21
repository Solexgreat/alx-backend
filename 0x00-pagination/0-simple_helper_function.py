#!/usr/bin/env python3
""" simple helper function """
from typing import Tuple


def index_range(page: int , page_size: int)-> Tuple[int, int]:
    """ function return the page and page_size in a
        tuple """
    i = page_size
    page_size = page_size * page
    page = page_size - i
    result = (page, page_size)
    return(result)
