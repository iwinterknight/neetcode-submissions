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


        def backtrack_efficient(candidates, target, start, curr, curr_sum, res):
            if curr_sum == target:
                res.append(curr[:])
                return

            if start >= len(candidates) or curr_sum > target:
                return

            prev = None
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num != prev:
                    curr.append(num)
                    curr_sum += num
                    backtrack_efficient(candidates, target, i+1, curr, curr_sum, res)
                    curr.pop()
                    curr_sum -= num
                    prev = num
            

        # res = []
        # backtrack(sorted(candidates), target, 0, [], 0, res)
        # return res

        res = []
        backtrack_efficient(sorted(candidates), target, 0, [], 0, res)
        return res