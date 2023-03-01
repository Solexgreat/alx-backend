from base_caching import BaseCaching
from typing import Union

class LIFOCache(BaseCaching):
    """
    """
    def __init__(self):
        super().__init__()
    
    def put(self, key: str, item: str) -> None:
        """
        """
        if key and item:
            self.CheckCache(key)
            self.cache_data[key] = item        
            
    def get(self, key: str) -> Union[None, object]:
        """
        """ 

        if key not in self.cache_data:
            return None
        return self.cache_data[key]
    
    def CheckCache(self, key: str) -> None:
        """
        """
        if len(self.cache_data.keys()) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                print(f"DISCARD: {self.cache_data.popitem()[0]}")
            else:
                del self.cache_data[key]


