# 模型训练中去计算准确率，tp/len(batch_size)
# input: y_pred : 10 * 3 [[0.1,0.2,0.7],[0.3,0.3,0.4]...]
# batch_size : 10 * 3(已经归一化)
# ground_truth : [1,1,0,1..]

import numpy as np
import torch

# numpy版本
def precision(y_pred, ground_truth):

    y_pred = np.argmax(y_pred, axis=1)
    return np.sum(y_pred == ground_truth) / ground_truth.size

# torch版本
def cal_precision(outputs,ground_truth):
    prob = torch.softmax(outputs, dim=1)
    _,pred_label = torch.max(prob, 1)
    return torch.sum(pred_label == ground_truth).item() / ground_truth.size(0)




