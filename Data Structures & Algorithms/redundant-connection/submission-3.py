class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent, rank = {}, {}
        for i in range(1, n+1):
            parent[i] = i
            rank[i] = 1


        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return [x, y]

            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[rx] = ry
                rank[rx] += 1

            return None

        for u, v in edges:
            if union(u, v):
                return [u, v]
        return []