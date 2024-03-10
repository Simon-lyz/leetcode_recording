nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return []
    nums_s = sorted(nums)
    res = []
    for i in range(len(nums)):
        l = i+1
        r = len(nums)-1
        while l < r and l > i:
            while l < r and nums_s[i] + nums_s[l] + nums_s[r] > 0:
                r -= 1
            while l < r and nums_s[i] + nums_s[l] + nums_s[r] < 0:
                l += 1
            if nums_s[i] + nums_s[l] + nums_s[r] == 0 and i != l and l != r and r != i:
                res.append([nums_s[i],nums_s[l],nums_s[r]])
                l += 1
                r -= 1
                print(nums_s[i])
                print(res)
    return list({tuple(inner_list): inner_list for inner_list in res}.values())


print(threeSum(nums))