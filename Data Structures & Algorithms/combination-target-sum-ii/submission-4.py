class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recursion(i=0, curr=[]):
            if sum(curr) == target and sorted(curr) not in res:
                res.append(sorted(curr[:]))
                return

            if i == len(candidates) or sum(curr) > target:
                return

            recursion(i+1, curr + [candidates[i]])
            recursion(i+1, curr)

        recursion()
        return res