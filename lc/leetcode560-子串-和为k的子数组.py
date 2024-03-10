def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # nums = sorted(nums)
    count = 0
    sums = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            sums[0] = nums[0]
        else:
            sums[i] = sums[i - 1] + nums[i]

    print(sums)
    for i in range(len(nums)):
        # print("sums[j] - sums[i]")
        for j in range(i, len(nums)):
            if i == 0:
                if k == sums[j]:
                    print(j,"",sum[j])
                    count += 1
                    # print(sums[j],"",sums[i-1],"",j,"",i)
            else:
                if k == sums[j] - sums[i - 1]:
                    count += 1

    return count
nums = [1]
k = 0
print()
print("cnt",subarraySum(nums,k))