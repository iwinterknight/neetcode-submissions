class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def recursion(i=0, curr=[], total=0):
            if total == target:
                res.append(curr[:])
                return

            if i == len(candidates) or total > target:
                return

            val = candidates[i]
            recursion(i+1, curr + [val], total + val)

            j = i+1
            while j < len(candidates) and candidates[j] == val:
                j += 1
            recursion(j, curr, total)

        recursion()
        return res