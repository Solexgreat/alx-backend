from base_caching import BaseCaching
from typing import Union

class MRUCache(BaseCaching):
    """
    """
    def __init__(self):
        self.recent_get =[]
        super().__init__()
    
    def put(self, key: str, item: str) -> None:
        """
        """
        if key and item:
            if key not in self.cache_data and len(self.cache_data.keys()) >= self.MAX_ITEMS:
                n = len(self.recent_get) - 1
                delete = self.recent_get[n]
                self.recent_get.remove(delete)
                del self.cache_data[delete]
                print(f"DISCARD: {delete}")   
            if key in self.recent_get:
                self.recent_get.remove(key)                
            self.cache_data[key] = item
            self.recent_get.append(key)
            
    def get(self, key: str) -> Union[None, object]:
        """
        """
        if key not in self.cache_data:
            return None
        self.recent_get.remove(key)
        self.recent_get.append(key)
        return self.cache_data[key]