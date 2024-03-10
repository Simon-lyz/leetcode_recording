
'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

# 子任务：helper(n-i-i,k-1)
'''
def dfs(n,k):
    res = []
    def helper(start,path):
        if len(path) == k:
            res.append(path[:])
            return

        for i in range(start,n+1):
            path.append(i)
            helper(i+1,path)
            path.pop()

    helper(1,[])
    return res

print(dfs(4,2))

# okr
# 1. pretrain + sft 基座模型的建设，算法老板主导，MMLU基础模型的建设。
# 2. 出行助手：LLM的应用 出行场景 -> Langchain Agent -> Agent中没有完备会反问用户。着力点是应用。
## 模型能力：推理计算+Agent能力
### 拆解指令 + 执行指令 -> 让模型写这个prompt -> 模型去反问用户

# 一周2~3会 10~21
# 多模态方面的工作，主要集中在NLP

## 个人劣势：基础+落地业务没有做的很深入。
## CTO牵头
'''
面试体验：80
面试收获：80

1. 种子数据怎么来，数量多大，如何过滤，多样性如何保证
2. 为什么不用测试集去跑epoch数做实验
3. 训练完后，如果使用常规问题进行回答（脱离场景）的结果是否有损？是否有做过无损sft的考虑？
4. 为什么不多跑几个epoch？应该跑得多效果好？
5. 三个模型的效果对比
6. 对base model做sft与对chat model（落地模型）去做sft有何区别
7. 为什么做这个任务的时候，不考虑base模型呢？
8. base model的训练学习的是什么？chat model学习的是什么？
9. langchain React有哪些了解？
10. langchain react基座模型怎么做选型？如果微调的话，sft数据该怎么去做？
11. Transformer LayerNorm 前置后置的效果区别以及作用的模型？为何能解决梯度的问题
12. 为什么要做ResNet？Pre LayerNorm和Post LayerNorm哪个和ResNet更像？
13. attention计算中除以根号dk的作用？
'''

'''
1. kbqa的工作流，base model选的是bert吗？每一步是怎么做的
2. bert系列模型你知道有哪些，讲讲
3. T5的训练方法
4. self-attention对比rnn
5. sft的数据是怎么来的？怎么做评估
6. 微调后的结果呈现一个怎样的形式
7. qlora和lora 在fp16下好像是一样的？为什么不直接用lora
8. peft有没有改过框架，还是直接用的现成框架
9. 三个模型呈现出的一个效果区别，为什么不用base模型而用chat模型
10. llama2参数量计算，head=10,layer=3,hidden=500（需要一步一步拆解模型的结构）
11. RAG生成阶段的评估是怎么做的？如何调整prompt让RAG的生成结果更好？
12. lora之前的peft微调方法有了解吗？

'''




