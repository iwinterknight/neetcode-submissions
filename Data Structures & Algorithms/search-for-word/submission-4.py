class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j, visited, matched):
            if board[i][j] == word[matched]:
                visited.add((i, j))
                matched += 1
            else:
                return False

            if matched == len(word):
                return True

            next_steps = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for step in next_steps:
                r, c = step[0], step[1]
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited:
                    if dfs(board, word, r, c, visited, matched):
                        return True
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, word, i, j, set(), 0):
                        return True
        return False
