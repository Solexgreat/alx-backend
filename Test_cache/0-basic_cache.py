#!/usr/bin/python3
""" 0-main """

from base_Caching import BaseCaching
from typing import Union


class BasicCache(BaseCaching):
    """
    """
    def put(self, key: str, item: str) -> None:
        """
        """
        if key and item:
            self.cache_data[key] = item
        
    def get(self, key: str) -> Union[None, object]:
        """
        """
        if key is not self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]


