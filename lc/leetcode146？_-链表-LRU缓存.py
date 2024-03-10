class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections
        self.capacity = capacity
        self.d = collections.OrderedDict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        else:
            value = self.d.pop(key)
            self.d[key] = value
            return value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.d.pop(key)
        self.d[key] = value
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)