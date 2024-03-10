input_list = [1,2,3,[2,3,[4,5],6]]
output = [1,2,3,2,3,4,5,6]


def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            # 如果是列表，递归调用 flatten_list 并扩展结果
            flattened.extend(flatten_list(item))
        else:
            # 如果不是列表，直接添加到结果中
            flattened.append(item)
    return flattened

# 示例
input_list = [1, 2, [2, 3, [4, 5], 6]]
output_list = flatten_list(input_list)
print("The flattened list is:", output_list)