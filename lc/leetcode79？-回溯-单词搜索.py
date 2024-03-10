class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        n = len(board)
        if n == 0:
            return False
        m = len(board[0])
        visited = set()
        def check(i,j,k):
            if board[i][j] != k:
                return False
            # 退出条件:
            if k == len(word)-1:
                return True

            mark = True
            visited.add((i,j))
            for di,dj in directions:
                ni,nj = i+di,j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    if (ni,nj) not in visited:
                        if check(ni,nj,k+1):
                            mark = True
                            break

            visited.remove((i,j))
            return mark
        for i in range(n):
            for j in range(m):
                if check(i,j,0):
                    return True

        return False



'''
result = []
def backtrack(选择列表, 路径):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表: (if not visited)
        # 做选择
        路径.add(选择)
        将该选择从选择列表移除

        
        backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】

        # 撤销选择
        路径.remove(选择)

        将该选择再加入选择列表
'''