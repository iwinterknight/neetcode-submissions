class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(board, word, r, c, idx, visited):
            if idx == len(word):
                return True

            visited.add((r, c))
            steps = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for step in steps:
                i, j = step[0], step[1]
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited and board[i][j] == word[idx]:
                    if backtrack(board, word, i, j, idx+1, visited):
                        return True
            visited.remove((r, c))
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(board, word, i, j, 1, set()):
                        return True
        return False