from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            """
                i,j当前元素在矩阵中的索引 k为word中匹配元素的索引
            """
            # 停止条件 i，j越界或者不匹配
            if not 0 <= i < len_row or not 0 <= j < len_col or board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            board[i][j] = ''
            res_flag = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = word[k]
            return res_flag

        len_row = len(board)
        len_col = len(board[0])
        for i in range(len_row):
            for j in range(len_col):
                if dfs(i, j, 0): return True
        return False



        return dfs(0, 0, 0)
            


if __name__=="__main__":
    solution = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    res = solution.exist(board, word)
    print(res)
