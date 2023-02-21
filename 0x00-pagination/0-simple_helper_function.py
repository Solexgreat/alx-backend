#!/usr/bin/env python3
""" simple helper function """
from typing import Tuple


def index_range(page: int , page_size: int)-> Tuple[int, int]:
    """
    function return the page and page_size in a tuple 
    """
    result = ((page - 1) * page_size, page_size * page)
    return(result)
