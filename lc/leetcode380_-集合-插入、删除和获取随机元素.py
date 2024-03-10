import random
class RandomizedSet(object):

    def __init__(self):
        self.list1 = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.list1:
            self.list1.append(val)
            return True
        else:
            return False


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.list1:
            self.list1.remove(val)
            return True
        else:
            return False


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list1)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()