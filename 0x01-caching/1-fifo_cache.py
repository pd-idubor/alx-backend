#!/usr/bin/python3
"""FIFO caching"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        """Initializer"""
        super().__init__()

    def put(self, key, item):
        """Assigns to dict the item value for the key"""
        if key and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > type(self).MAX_ITEMS:
            first = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first))
            del(self.cache_data[first])

    def get(self, key):
        """Returns thr value of cache_data key"""
        if key and self.cache_data.get(key) is not None:
            return self.cache_data[key]
