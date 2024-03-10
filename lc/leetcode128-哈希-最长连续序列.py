def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    print(num_set)
    longest_streak = 0

    for num in num_set:
        # 只有当当前数字是连续序列的起始点时才开始查找
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# 测试示例
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

output1 = longest_consecutive(nums1)
output2 = longest_consecutive(nums2)

print(output1)
print(output2)


