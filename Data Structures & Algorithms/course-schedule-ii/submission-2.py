class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        for course, preq in prerequisites:
            premap[course].append(preq)

        def topological_sort(course, completed, res, visit=set()):
            if course in completed:
                return True
            visit.add(course)
            for preq in premap[course]:
                if preq in visit:
                    return False
                if not topological_sort(preq, completed, res):
                    return False
            visit.remove(course)
            completed.add(course)
            res.append(course)
            return True

        completed = set()
        res = []
        for course in range(numCourses):
            if course not in completed:
                if not topological_sort(course, completed, res):
                    return []
        return res