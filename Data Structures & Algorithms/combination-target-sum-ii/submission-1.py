class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, i, curr, curr_sum, res):
            if curr_sum == target:
                if curr not in res:
                    res.append(curr[:])
                return

            if i >= len(candidates) or curr_sum > target:
                return

            curr_sum += candidates[i]
            curr.append(candidates[i])
            backtrack(candidates, target, i+1, curr, curr_sum, res)
            curr_sum -= candidates[i]
            curr.pop()
            backtrack(candidates, target, i+1, curr, curr_sum, res)

        res = []
        backtrack(sorted(candidates), target, 0, [], 0, res)
        return res