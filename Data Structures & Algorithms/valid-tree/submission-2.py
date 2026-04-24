class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for s, t in edges:
            adj[s].append(t)
            adj[t].append(s)

        completed = set()

        def dfs(s, parent, visit=set()):
            if s in visit:
                return False
            visit.add(s)
            for t in adj[s]:
                if t == parent:
                    continue
                if not dfs(t, s, visit):
                    return False
            completed.add(s)
            return True

        if n > 0:
            if not dfs(0, -1):
                return False
            if len(completed) < n:
                return False
            
        return True