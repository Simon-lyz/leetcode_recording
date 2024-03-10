class Solution:
    def solveNQueens(self, n):
        m = n * 2 - 1
        ans = []
        col = [0] * n
        # 使用三个集合 columns、diag1、diag2分别记录每一列以及两个方向的每条斜线上是否有皇后。
        on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m

        def dfs(r):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
                return
            for c, on in enumerate(on_path):

                if not on and not diag1[r + c] and not diag2[r - c]:
                    col[r] = c
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans



    def solveNQueens1(self,n):
        m = 2*n-1
        ans = []
        col = [0] * n
        onpath,diag1,diag2 = [False]*n , [False] * m,[False]*m
        def dfs(r):
            if r == n:
                ans.append(["."*c + 'Q' + "."*(n-1-c) for c in col])
                return
            for c,on in enumerate(onpath):
                if not on and not diag1[r+c] and not diag2[r+c]:
                    col[r] = c
                    onpath[c] = diag1[r+c] = diag2[r-c] = True
                    dfs(r+1)
                    onpath[c] = diag1[r + c] = diag2[r - c] = False

        dfs(0)
        return ans