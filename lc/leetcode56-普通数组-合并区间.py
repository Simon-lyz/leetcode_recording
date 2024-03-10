
def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    list1 = sorted(intervals,key=lambda x:x[0])
    reslist = [list1[0]]
    for i in range(len(list1)):
        startidx = list1[i][0]
        endidx = list1[i][1]
        print(reslist)
        if not reslist or reslist[-1][1] < startidx:
            reslist.append(list1[i])
        else:
            reslist[-1][1] = max(reslist[-1][1],list1[i][1])
    return reslist



intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
