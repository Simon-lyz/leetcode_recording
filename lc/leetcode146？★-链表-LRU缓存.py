import collections
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.d = collections.OrderedDict()

    def get(self, key):
        if key not in self.d:
            return -1
        else:
            value = self.d.pop(key)
            self.d[key] = value
            return value

    def put(self, key, value):
        if key in self.d:
            self.d.pop(key)
        self.d[key] = value
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)

