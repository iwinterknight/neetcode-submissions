class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for course, preq in prerequisites:
            pre_map[course].append(preq)
        
        def dfs(course, visit=set()):
            visit.add(course)
            for preq in pre_map[course]:
                if preq in visit:
                    return False
                if not dfs(preq, visit):
                    return False
            visit.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True