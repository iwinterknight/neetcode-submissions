class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        q = deque()
        
        def scan(r, c, visit):
            residual = deque()
            q.append((r, c))
            visit.add((r, c))
            residual.append((r, c))
            surrounded = True
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    residual.append((r, c))

                    for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if i < 0 or i == R or j < 0 or j == C:
                            print(i, j)
                            surrounded = False
                        elif board[i][j] == "O" and (i, j) not in visit:
                            q.append((i, j))
                            visit.add((i, j))

            if surrounded:
                for i, j in residual:
                    board[i][j] = "X"

        visit = set()
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O" and (i, j) not in visit:
                    visit.add((i, j))
                    scan(i, j, visit)