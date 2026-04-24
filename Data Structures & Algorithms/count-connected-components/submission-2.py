class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, t in edges:
            adj[s].append(t)
            adj[t].append(s)

        def dfs(s, parent, processed, visited=set()):
            visited.add(s)
            for t in adj[s]:
                if t == parent:
                    continue
                if t not in visited:
                    dfs(t, s, processed, visited)
            processed.add(s)

        processed = set()
        components = 0
        for i in range(n):
            if i not in processed:
                dfs(i, -1, processed)
                components += 1

        return components