

# input1 = [1,2,3]
# output1 = [2,1,3]

def help(nums):
    n = len(nums)
    # find最大索引

    max_index = -1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            max_index = i
            break

    print(max_index)

    def reverse(nums,i,j):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1

    if max_index == -1:
        reverse(nums,0,n-1)
        return nums

    # 第二个索引如果被找到，那就交换[max_index+1:]
    second_index = -1
    for i in range(n-1,max_index,-1):
        if nums[i] > nums[max_index]:
            second_index = i
            break
    nums[max_index],nums[second_index] = nums[second_index],nums[max_index]
    reverse(nums,max_index+1,n-1)
    return nums

print(help([1,3,2]))



