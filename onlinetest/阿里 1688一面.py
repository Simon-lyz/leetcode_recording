import numpy as np
# numpy转list



def softmax(logits, mask, weights):
    # 应用权重到 logits
    # 两个list相乘
    weighted_logits = [a*b for a,b in zip(logits, weights)]

    print(weighted_logits)

    # 忽略 mask 中值为 0 的 logits
    masked_logits = [logit for logit, mask_value in zip(weighted_logits, mask) if mask_value == 1]

    # 如果没有有效的 logits（即 masked_logits 为空），则返回一个全为 0 的列表
    if not masked_logits:
        return [0] * len(logits)

    logits = logits - np.max(logits)

    # 计算 softmax
    exp_logits = np.exp(np.array(masked_logits))
    softmax_weights = exp_logits / (np.sum(exp_logits)+1e-9)

    return softmax_weights

# 示例使用
logits = [1, 1, 1, 1, 1]
mask = [1, 1, 0, 0, 0]
weights = [0.5, 0.5, 0, 0, 0]

softmax_weights = softmax(logits, mask, weights)
print(softmax_weights)

# numpy转list


class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root












