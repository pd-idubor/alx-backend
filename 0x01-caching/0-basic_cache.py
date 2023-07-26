#!/usr/bin/python3
"""Defines a class BasicCache that is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching system"""
    def put(self, key, item):
        """Assigns to dict the item value for the key"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns thr value of cache_data key"""
        if key and self.cache_data.get(key) is not None:
            return self.cache_data[key]
