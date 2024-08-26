class CachingService:
    def __init__(self):
        self.cache = {} 

    def cache_result(self, key, value):
        self.cache[key] = value

    def get_cached_result(self, key):
        return self.cache.get(key)

    def has_changed(self, key, value):
        return self.cache.get(key) != value
