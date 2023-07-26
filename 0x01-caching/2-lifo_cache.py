#!/usr/bin/python3
"""LIFO caching"""
from collections import OrderedDict
BaseCaching = __import__('0-basic_cache').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """Initializer"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns to dict the item value for the key"""
        if len(self.cache_data) >= type(self).MAX_ITEMS:
            last = next(reversed(self.cache_data))
            print("DISCARD: {}".format(last))
            del(self.cache_data[last])
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of cache_data key"""
        if key and self.cache_data.get(key) is not None:
            return self.cache_data[key]
