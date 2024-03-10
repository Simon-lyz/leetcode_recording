class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        dict1 = dict(collections.Counter(nums))
        # 找最大的key
        return max(dict1,key=dict1.get)

        # 找最大的value
        # return max(dict1.values())

        # sorted 按照strlen排序
        # words = ['apple', 'banana', 'cherry', 'date']
        # sorted_words = sorted(words, key=len)
        # print(sorted_words)  # 输出: ['date', 'apple', 'cherry', 'banana']


        # 使用sorted函数和字典的keys方法对键进行排序
        # sorted_keys = sorted(dict_data, key=dict_data.keys)
        # print(sorted_keys)  # 输出: ['key1', 'key2', 'key3']

        # dict值排序：使用sorted函数和字典的get方法对值进行排序
        #sorted_values = sorted(dict_data.items(), key=lambda item: item[1])
        #print(sorted_values)  # 输出: [('key2', 10), ('key3', 20), ('key1', 30)]

        # 使用sorted函数和字典的get方法对值进行降序排序
        #sorted_values = sorted(dict_data.items(), key=lambda item: item[1], reverse=True)
        #print(sorted_values)  # 输出: [('key1', 30), ('key3', 20), ('key2', 10)]

        # 使用sorted函数和字典的get方法对值进行降序排序，并只提取排序后的键
        # sorted_keys = [key for key, _ in sorted(dict_data.items(), key=lambda item: item[1], reverse=True)]