class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, visited=set(), curr=""):
            if curr == word:
                return True

            visited.add((r, c))

            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + i, c + j
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and (new_r, new_c) not in visited and len(curr) < len(word):
                    if dfs(new_r, new_c, visited, curr + board[new_r][new_c]):
                        return True
            
            visited.remove((r, c))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, set(), board[i][j]):
                        return True
        return False
