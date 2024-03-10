nums = [0,1,0,3,12]
def moveZeroes(nums):
    if not nums:
        return 0
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j],nums[i] = nums[i],nums[j]
            j += 1
    return nums

print(moveZeroes(nums))