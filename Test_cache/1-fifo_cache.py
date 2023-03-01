
from base_caching import BaseCaching
from typing import Union

class FIFOCache(BaseCaching):
    """
    """
    def __init__(self):
        super().__init__()
    
    def put(self, key: str, item: str) -> None:
        """
        """
        if key and item:
           self.cache_data[key] = item
        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")
        
        """self.cache_data.popitem"""
    def get(self, key: str) -> Union[None, object]:
        """
        """ 

        if key not in self.cache_data:
            return None
        return self.cache_data[key]