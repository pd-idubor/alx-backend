#!/usr/bin/python3
"""LRU caching"""
from collections import OrderedDict
BaseCaching = __import__('0-basic_cache').BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""
    def __init__(self):
        """Initializer"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns to dict the item value for the key"""
        if key and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= type(self).MAX_ITEMS:
                lru, val = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(lru))
            self.cache_data[key] = item

    def get(self, key):
        """Returns thr value of cache_data key"""
        if key and self.cache_data.get(key) is not None:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
